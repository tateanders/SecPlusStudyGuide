#!/usr/bin/env python3
"""Build HOW_TO_USE.pdf from docs/HOW_TO_USE.md.

Needs the dev requirements (fpdf2, markdown):
    cd app && python3 -m venv .venv-dev && .venv-dev/bin/pip install -r requirements-dev.txt
    app/.venv-dev/bin/python app/tools/build_pdf.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import markdown
from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[2]  # the Study Guide folder
SRC = ROOT / "app" / "docs" / "HOW_TO_USE.md"
OUT = ROOT / "HOW_TO_USE.pdf"

# The built-in PDF fonts only cover Latin-1, so swap the few symbols the guide uses.
REPLACE = {
    "→": "->", "←": "<-", "↑": "Up", "↓": "Down", "–": "-", "—": " - ", "‘": "'", "’": "'",
    "“": '"', "”": '"', "…": "...", "✓": "(check)", "✗": "(x)", "•": "-", "≥": ">=", "≤": "<=",
}


def latin1(text: str) -> str:
    for a, b in REPLACE.items():
        text = text.replace(a, b)
    return text.encode("latin-1", "replace").decode("latin-1")


class Guide(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", size=8)
        self.set_text_color(130)
        self.cell(0, 8, f"How to Use the Study App  -  page {self.page_no()}", align="C")


def build() -> Path:
    md = latin1(SRC.read_text(encoding="utf-8"))
    html = markdown.markdown(md, extensions=["tables", "fenced_code"])
    # fpdf2's HTML renderer: give tables full width and borders, and keep code blocks monospace.
    html = html.replace("<table>", '<table width="100%" border="1">')
    html = re.sub(r"<pre><code[^>]*>", "<pre>", html).replace("</code></pre>", "</pre>")

    pdf = Guide(format="Letter")
    pdf.set_margins(18, 16, 18)
    pdf.set_auto_page_break(True, margin=16)
    pdf.add_page()
    pdf.set_font("Helvetica", size=10.5)
    pdf.write_html(html, tag_styles=None, table_line_separators=True)
    pdf.output(str(OUT))
    return OUT


if __name__ == "__main__":
    try:
        print(f"Wrote {build()}")
    except Exception as e:  # make failures obvious when run by hand
        print(f"PDF build failed: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
