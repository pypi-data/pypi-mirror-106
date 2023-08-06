#  Copyright (c) 2021, Manfred Moitzi
#  License: MIT License
from typing import cast, Dict, Tuple, List
import sys
import math
import ezdxf
from ezdxf.entities import MText, DXFGraphic, Textstyle
from ezdxf.layouts import BaseLayout
from ezdxf.math import Matrix44
from ezdxf.tools import text_layout, fonts
from ezdxf.tools.text import (
    MTextParser, MTextContext, TokenType, MTextParagraphAlignment,
)

__all__ = ["MTextExplode"]

if not ezdxf.options.use_matplotlib:
    print("The Matplotlib package is required.")
    sys.exit(1)


class FrameRenderer(text_layout.ContentRenderer):
    def __init__(self, attribs: Dict, layout: BaseLayout):
        self.line_attribs = attribs
        self.layout = layout

    def render(self, left: float, bottom: float, right: float,
               top: float, m: Matrix44 = None) -> None:
        pline = self.layout.add_lwpolyline(
            [(left, top), (right, top), (right, bottom), (left, bottom)],
            close=True, dxfattribs=self.line_attribs,
        )
        if m:
            pline.transform(m)

    def line(self, x1: float, y1: float, x2: float, y2: float,
             m: Matrix44 = None) -> None:
        line = self.layout.add_line((x1, y1), (x2, y2),
                                    dxfattribs=self.line_attribs)
        if m:
            line.transform(m)


class ColumnBackgroundRenderer(FrameRenderer):
    def __init__(self, attribs: Dict, layout: BaseLayout,
                 bg_aci: int = None,
                 bg_true_color: int = None,
                 offset: float = 0,
                 text_frame: bool = False):
        super().__init__(attribs, layout)
        self.solid_attribs = None
        if bg_aci is not None:
            self.solid_attribs = dict(attribs)
            self.solid_attribs["color"] = bg_aci
        elif bg_true_color is not None:
            self.solid_attribs = dict(attribs)
            self.solid_attribs["true_color"] = bg_true_color
        self.offset = offset  # background border offset
        self.has_text_frame = text_frame

    def render(self, left: float, bottom: float, right: float,
               top: float, m: Matrix44 = None) -> None:
        # Important: this is not a clipping box, it is possible to
        # render anything outside of the given borders!
        offset = self.offset
        left -= offset
        right += offset
        top += offset
        bottom -= offset
        if self.solid_attribs is not None:
            solid = self.layout.add_solid(
                # SOLID! switch last two vertices:
                [(left, top), (right, top), (left, bottom), (right, bottom)],
                dxfattribs=self.solid_attribs,
            )
            if m:
                solid.transform(m)
        if self.has_text_frame:
            super().render(left, bottom, right, top, m)


class TextRenderer(FrameRenderer):
    """ Text content renderer. """

    def __init__(self, text: str, text_attribs: Dict, line_attribs: Dict,
                 layout: BaseLayout):
        super().__init__(line_attribs, layout)
        self.text = text
        self.text_attribs = text_attribs

    def render(self, left: float, bottom: float, right: float,
               top: float, m: Matrix44 = None):
        """ Create/render the text content """
        text = self.layout.add_text(self.text, dxfattribs=self.text_attribs)
        text.set_pos((left, bottom), align='LEFT')
        if m:
            text.transform(m)


class Word(text_layout.Text):
    """ Represent a word as content box for the layout engine. """

    def __init__(self, text: str, ctx: MTextContext, attribs: Dict,
                 xpl: "MTextExplode"):
        # Each content box can have individual properties:
        line_attribs = dict(attribs or {})
        line_attribs.update(get_color_attribs(ctx))
        text_attribs = dict(line_attribs)
        text_attribs.update(xpl.get_text_attribs(ctx))

        font = xpl.get_font(ctx)
        stroke = get_stroke(ctx)
        super().__init__(
            # Width and height of the content are fixed given values and will
            # not be changed by the layout engine:
            width=font.text_width(text),
            height=ctx.cap_height,
            valign=text_layout.CellAlignment(ctx.align),
            stroke=stroke,
            # Each content box can have it's own rendering object:
            renderer=TextRenderer(text, text_attribs, line_attribs, xpl.layout),
        )


STACKING = {
    "^": text_layout.Stacking.OVER,
    "/": text_layout.Stacking.LINE,
    "#": text_layout.Stacking.SLANTED,
}


class Fraction(text_layout.Fraction):
    def __init__(self, upr: str, lwr: str, type_: str, ctx: MTextContext,
                 attribs: Dict, xpl: "MTextExplode"):
        super().__init__(
            top=Word(upr, ctx, attribs, xpl),
            bottom=Word(lwr, ctx, attribs, xpl),
            stacking=STACKING.get(type_, text_layout.Stacking.LINE),
            # Uses only the generic line renderer to render the divider line,
            # the top- and bottom content boxes use their own render objects.
            renderer=FrameRenderer(attribs, xpl.layout),
        )


def get_font_face(entity: DXFGraphic, doc=None) -> fonts.FontFace:
    """ Returns the :class:`~ezdxf.tools.fonts.FontFace` defined by the
    associated text style. Returns the default font face if the `entity` does
    not have or support the DXF attribute "style".

    Pass a DXF document as argument `doc` to resolve text styles for virtual
    entities which are not assigned to a DXF document. The argument `doc`
    always overrides the DXF document to which the `entity` is assigned to.

    """
    if entity.doc and doc is None:
        doc = entity.doc
    assert doc is not None, "DXF document required"

    style_name = ""
    # This also works for entities which do not support "style",
    # where :code:`style_name = entity.dxf.get("style")` would fail.
    if entity.dxf.is_supported("style"):
        style_name = entity.dxf.style

    font_face = fonts.FontFace()
    if style_name and doc is not None:
        style = cast(Textstyle, doc.styles.get(style_name))
        family, italic, bold = style.get_extended_font_data()
        if family:
            text_style = "italic" if italic else "normal"
            text_weight = "bold" if bold else "normal"
            font_face = fonts.FontFace(
                family=family, style=text_style, weight=text_weight)
        else:
            ttf = style.dxf.font
            if ttf:
                font_face = fonts.get_font_face(ttf)
    return font_face


def mtext_context(mtext: MText) -> MTextContext:
    """ Setup initial MTEXT context. """
    ctx = MTextContext()
    ctx.font_face = get_font_face(mtext)
    ctx.cap_height = mtext.dxf.char_height
    ctx.color = mtext.dxf.color
    rgb = mtext.rgb
    if rgb is not None:
        ctx.rgb = rgb
    return ctx


ALIGN = {
    MTextParagraphAlignment.LEFT: text_layout.FlowTextAlignment.LEFT,
    MTextParagraphAlignment.RIGHT: text_layout.FlowTextAlignment.RIGHT,
    MTextParagraphAlignment.CENTER: text_layout.FlowTextAlignment.CENTER,
    MTextParagraphAlignment.JUSTIFIED: text_layout.FlowTextAlignment.JUSTIFIED,
    MTextParagraphAlignment.DISTRIBUTED: text_layout.FlowTextAlignment.JUSTIFIED,
    MTextParagraphAlignment.DEFAULT: text_layout.FlowTextAlignment.LEFT,
}


def new_paragraph(cells: List, ctx: MTextContext, cap_height: float,
                  line_spacing: float = 1):
    if cells:
        p = ctx.paragraph
        align = ALIGN.get(p.align, text_layout.FlowTextAlignment.LEFT)
        left = p.left * cap_height
        right = p.right * cap_height
        first = left + p.indent * cap_height  # relative to left
        paragraph = text_layout.FlowText(
            align=align,
            indent=(first, left, right),
            line_spacing=line_spacing,
        )
        paragraph.append_content(cells)
    else:
        paragraph = text_layout.EmptyParagraph(
            cap_height=ctx.cap_height, line_spacing=line_spacing)
    return paragraph


def get_stroke(ctx: MTextContext) -> int:
    stroke = 0
    if ctx.underline:
        stroke += text_layout.Stroke.UNDERLINE
    if ctx.strike_through:
        stroke += text_layout.Stroke.STRIKE_THROUGH
    if ctx.overline:
        stroke += text_layout.Stroke.OVERLINE
    return stroke


def get_color_attribs(ctx: MTextContext) -> Dict:
    attribs = {"color": ctx.aci}
    if ctx.rgb is not None:
        attribs["true_color"] = ezdxf.rgb2int(ctx.rgb)
    return attribs


def super_glue():
    return text_layout.NonBreakingSpace(width=0, min_width=0, max_width=0)


def make_bg_renderer(mtext: MText, attribs: Dict, layout: BaseLayout):
    dxf = mtext.dxf
    bg_fill = dxf.get("bg_fill", 0)

    bg_aci = None
    bg_true_color = None
    has_text_frame = False
    offset = 0
    if bg_fill:
        # The fill scale is a multiple of the initial char height and
        # a scale of 1, fits exact the outer border
        # of the column -> offset = 0
        offset = dxf.char_height * (dxf.get("box_fill_scale", 1.5) - 1)
        if bg_fill & ezdxf.const.MTEXT_BG_COLOR:
            if dxf.hasattr("bg_fill_color"):
                bg_aci = dxf.bg_fill_color

            if dxf.hasattr("bg_fill_true_color"):
                bg_aci = None
                bg_true_color = dxf.bg_fill_true_color

            if (bg_fill & 3) == 3:  # canvas color = bit 0 and 1 set
                # can not detect canvas color from DXF document!
                # do not draw any background:
                bg_aci = None
                bg_true_color = None

        if bg_fill & ezdxf.const.MTEXT_TEXT_FRAME:
            has_text_frame = True

    return ColumnBackgroundRenderer(
        attribs, layout,
        bg_aci=bg_aci,
        bg_true_color=bg_true_color,
        offset=offset,
        text_frame=has_text_frame,
    )


class MTextExplode:
    def __init__(self, layout: BaseLayout, doc=None,
                 spacing_factor: float = 1.0):
        self.layout = layout
        self._doc = doc if doc else layout.doc
        assert self._doc is not None, "DXF document required"
        # scale the width of spaces by this factor:
        self._spacing_factor = spacing_factor
        self._required_text_styles: Dict = {}
        self._font_cache = {}

    def mtext_exploded_text_style(self, font_face: fonts.FontFace) -> str:
        style = 0
        if font_face.is_bold:
            style += 1
        if font_face.is_italic:
            style += 2
        style = str(style) if style > 0 else ""
        # BricsCAD naming convention for exploded MTEXT styles:
        text_style = f"MtXpl_{font_face.family}" + style
        self._required_text_styles[text_style] = font_face
        return text_style

    def get_font(self, ctx: MTextContext) -> fonts.AbstractFont:
        ttf = fonts.find_ttf_path(ctx.font_face)
        key = (ttf, ctx.cap_height, ctx.width_factor)
        font = self._font_cache.get(key)
        if font is None:
            font = fonts.make_font(ttf, ctx.cap_height, ctx.width_factor)
            self._font_cache[key] = font
        return font

    def get_text_attribs(self, ctx: MTextContext) -> Dict:
        attribs = {
            "height": ctx.cap_height,
            "style": self.mtext_exploded_text_style(ctx.font_face),
        }
        if not math.isclose(ctx.width_factor, 1.0):
            attribs["width"] = ctx.width_factor
        if abs(ctx.oblique) > 1e-6:
            attribs["oblique"] = ctx.oblique
        return attribs

    def layout_engine(self, mtext: MText) -> text_layout.Layout:
        def get_base_attribs() -> Dict:
            dxf = mtext.dxf
            attribs = {
                "layer": dxf.layer,
                "color": dxf.color,
            }
            return attribs

        def append_paragraph():
            paragraph = new_paragraph(
                cells, ctx, initial_cap_height, line_spacing)
            layout.append_paragraphs([paragraph])
            cells.clear()

        def column_heights():
            if columns.heights:  # dynamic manual
                heights = list(columns.heights)
                # last height has to be auto height = None
                heights[-1] = None
            else:  # static, dynamic auto
                heights = [columns.defined_height] * columns.count
            return heights

        content = mtext.all_columns_raw_content()
        initial_cap_height = mtext.dxf.char_height
        # same line spacing for all paragraphs
        line_spacing = mtext.dxf.line_spacing_factor
        base_attribs = get_base_attribs()
        ctx = mtext_context(mtext)
        parser = MTextParser(content, ctx)
        bg_renderer = make_bg_renderer(mtext, base_attribs, self.layout)
        layout = text_layout.Layout(width=mtext.dxf.width)
        if mtext.has_columns:
            columns = mtext.columns
            for height in column_heights():
                layout.append_column(
                    width=columns.width,
                    height=height,
                    gutter=columns.gutter_width,
                    renderer=bg_renderer,
                )
        else:
            # column with auto height and default width
            layout.append_column(renderer=bg_renderer)

        cells = []
        for token in parser:
            ctx = token.ctx
            if token.type == TokenType.NEW_PARAGRAPH:
                append_paragraph()
            elif token.type == TokenType.NEW_COLUMN:
                append_paragraph()
                layout.next_column()
            elif token.type == TokenType.SPACE:
                cells.append(self.space(ctx))
            elif token.type == TokenType.NBSP:
                cells.append(self.non_breaking_space(ctx))
            elif token.type == TokenType.TABULATOR:
                cells.append(self.space(ctx))
            elif token.type == TokenType.WORD:
                if cells and isinstance(cells[-1], Word):
                    # property change inside a word, create an unbreakable
                    # connection between those two parts of the same word.
                    cells.append(super_glue())
                cells.append(self.word(token.data, ctx, base_attribs))
            elif token.type == TokenType.STACK:
                cells.append(self.fraction(token.data, ctx, base_attribs))

        if cells:
            append_paragraph()

        return layout

    def space_width(self, ctx: MTextContext) -> float:
        return self.get_font(ctx).space_width() * self._spacing_factor

    def space(self, ctx: MTextContext):
        return text_layout.Space(width=self.space_width(ctx))

    def non_breaking_space(self, ctx: MTextContext):
        return text_layout.NonBreakingSpace(width=self.space_width(ctx))

    def word(self, text: str, ctx: MTextContext, attribs: Dict):
        return Word(text, ctx, attribs, self)

    def fraction(self, data: Tuple, ctx: MTextContext, attribs: Dict):
        upr, lwr, type_ = data
        if type_:
            return Fraction(upr, lwr, type_, ctx, attribs, self)
        else:
            return Word(upr, ctx, attribs, self)

    def explode(self, mtext: MText, destroy=True):
        align = text_layout.LayoutAlignment(mtext.dxf.attachment_point)
        layout_engine = self.layout_engine(mtext)
        layout_engine.place(align=align)
        layout_engine.render(mtext.ucs().matrix)
        if destroy:
            mtext.destroy()

    def finalize(self):
        def ttf_path(font_face: fonts.FontFace) -> str:
            ttf = font_face.ttf
            if not ttf:
                ttf = fonts.find_ttf_path(font_face)
            else:
                # remapping SHX replacement fonts to SHX fonts,
                # like "txt_____.ttf" to "TXT.SHX":
                shx = fonts.map_ttf_to_shx(ttf)
                if shx:
                    ttf = shx
            return ttf

        text_styles = self._doc.styles
        for name, font_face in self._required_text_styles.items():
            if name not in text_styles:
                style = cast(Textstyle, text_styles.new(name))
                ttf = ttf_path(font_face)
                style.dxf.font = ttf
                if not ttf.endswith(".SHX"):
                    style.set_extended_font_data(
                        font_face.family,
                        italic=font_face.is_italic,
                        bold=font_face.is_bold,
                    )
