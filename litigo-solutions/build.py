#!/usr/bin/env python3
"""Build the Litigo landing page into a single self-contained index.html.

Fonts are subset to the glyphs the page actually uses, converted to woff2 and
inlined as data URIs, because the hosting target blocks external font requests.

Usage:  python3 build.py
"""

from __future__ import annotations

import base64
import io
import pathlib
import re
import sys

try:
    from fontTools.subset import Subsetter, Options
    from fontTools.ttLib import TTFont
except ImportError:  # pragma: no cover
    sys.exit("Missing dependency. Run: pip install fonttools brotli")

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "page.html"
OUT = ROOT / "index.html"
FONT_DIR = ROOT / "fonts"

# family, style, weight, file
FACES = [
    ("Plex Serif", "normal", 400, "IBMPlexSerif-Regular.ttf"),
    ("Plex Serif", "normal", 700, "IBMPlexSerif-Bold.ttf"),
    ("Plex Serif", "italic", 400, "IBMPlexSerif-Italic.ttf"),
    ("Instrument", "normal", 400, "InstrumentSans-Regular.ttf"),
    ("Instrument", "normal", 700, "InstrumentSans-Bold.ttf"),
    ("Plex Mono", "normal", 400, "IBMPlexMono-Regular.ttf"),
    ("Plex Mono", "normal", 700, "IBMPlexMono-Bold.ttf"),
]

# Latin + the German set the copy needs, plus typographic and UI marks.
EXTRA_CHARS = (
    "ÄÖÜäöüßẞ"
    "áàâéèêíìîóòôúùûñçÁÀÂÉÈÊÍÌÎÓÒÔÚÙÛÑÇ"
    "€§©®°%‰&@#*+−×÷=≈≤≥~^|"
    "„“”‚‘’«»›‹\"'"
    "–—…·•→←↑↓⟶✓✗№"
    "()[]{}<>/\\"
)


def glyph_text(html: str) -> str:
    """Every character the built page can render, plus a safety margin."""
    text = re.sub(r"<[^>]+>", " ", html)
    printable = "".join(chr(c) for c in range(0x20, 0x7F))
    return printable + EXTRA_CHARS + text


def subset_face(path: pathlib.Path, text: str) -> bytes:
    font = TTFont(str(path))
    options = Options()
    options.flavor = "woff2"
    options.layout_features = ["kern", "liga", "calt", "tnum", "onum", "ccmp", "locl"]
    options.desubroutinize = True
    options.drop_tables += ["DSIG"]
    options.name_IDs = ["*"]
    options.name_legacy = True
    options.notdef_outline = True
    options.recalc_bounds = True
    subsetter = Subsetter(options=options)
    subsetter.populate(text=text)
    subsetter.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    font.close()
    return buf.getvalue()


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    text = glyph_text(html)

    blocks: list[str] = []
    total = 0
    for family, style, weight, filename in FACES:
        data = subset_face(FONT_DIR / filename, text)
        total += len(data)
        b64 = base64.b64encode(data).decode("ascii")
        blocks.append(
            "@font-face{"
            f"font-family:'{family}';"
            f"font-style:{style};"
            f"font-weight:{weight};"
            "font-display:block;"
            f"src:url(data:font/woff2;base64,{b64}) format('woff2')"
            "}"
        )
        print(f"  {filename:<28} {len(data) / 1024:6.1f} KB")

    if "<!--FONTS-->" not in html:
        sys.exit("src/page.html is missing the <!--FONTS--> placeholder")

    OUT.write_text(html.replace("<!--FONTS-->", "\n".join(blocks)), encoding="utf-8")
    print(f"\n  fonts  {total / 1024:.1f} KB")
    print(f"  wrote  {OUT.relative_to(ROOT)}  ({OUT.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
