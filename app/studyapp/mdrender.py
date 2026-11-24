"""A small, safe markdown renderer for question text.

Supports paragraphs, line breaks, headings, bullet/numbered lists, pipe tables,
fenced code blocks, blockquotes, **bold**, *italic*, and `inline code`.
All text is HTML-escaped before any markup is added.
"""
from __future__ import annotations

import html
import re

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})\s*([\w+-]*)\s*$")
UL_RE = re.compile(r"^\s*[-*+]\s+(.*)$")
OL_RE = re.compile(r"^\s*\d+[.)]\s+(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def inline(text: str) -> str:
    """Render inline markdown (code spans, bold, italic) on one piece of text."""
    out = []
    parts = re.split(r"(`+)(.+?)\1", text)
    # re.split with two groups yields: text, ticks, code, text, ticks, code, ...
    i = 0
    while i < len(parts):
        out.append(_emphasis(html.escape(parts[i], quote=False)))
        if i + 2 < len(parts):
            out.append("<code>" + html.escape(parts[i + 2].strip(), quote=False) + "</code>")
        i += 3
    return "".join(out)


def _emphasis(s: str) -> str:
    s = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"__(?=\S)(.+?)(?<=\S)__", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_(?=\S)(.+?)(?<=\S)_(?![\w_])", r"<em>\1</em>", s)
    return s


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def render(md: str) -> str:
    if not md:
        return ""
    lines = md.splitlines()
    out: list[str] = []
    para: list[str] = []
    i = 0

    def flush_para():
        if para:
            out.append("<p>" + "<br>".join(inline(p.strip()) for p in para) + "</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]
        m = FENCE_RE.match(line)
        if m:
            flush_para()
            fence = m.group(1)
            lang = m.group(2)
            code = []
            i += 1
            while i < len(lines) and not (lines[i].strip().startswith(fence[0] * len(fence))
                                          and lines[i].strip().strip(fence[0]) == ""):
                code.append(lines[i])
                i += 1
            i += 1
            cls = f' class="lang-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>" + html.escape("\n".join(code), quote=False) + "</code></pre>")
            continue
        if not line.strip():
            flush_para()
            i += 1
            continue
        hm = HEADING_RE.match(line)
        if hm:
            flush_para()
            level = min(len(hm.group(1)) + 2, 6)  # keep headings inside questions small
            out.append(f"<h{level}>{inline(hm.group(2))}</h{level}>")
            i += 1
            continue
        if "|" in line and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]):
            flush_para()
            head = _split_row(line)
            i += 2
            rows = []
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append(_split_row(lines[i]))
                i += 1
            t = ["<table><thead><tr>"] + [f"<th>{inline(c)}</th>" for c in head] + ["</tr></thead><tbody>"]
            for r in rows:
                t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            t.append("</tbody></table>")
            out.append("".join(t))
            continue
        if UL_RE.match(line) or OL_RE.match(line):
            flush_para()
            ordered = bool(OL_RE.match(line)) and not UL_RE.match(line)
            rx = OL_RE if ordered else UL_RE
            items: list[str] = []
            while i < len(lines) and lines[i].strip():
                im = rx.match(lines[i])
                if im:
                    items.append(im.group(1))
                elif lines[i][:1] in " \t" and items:
                    items[-1] += " " + lines[i].strip()
                else:
                    break
                i += 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(it)}</li>" for it in items) + f"</{tag}>")
            continue
        if line.lstrip().startswith(">"):
            flush_para()
            quote = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                quote.append(lines[i].lstrip()[1:].lstrip())
                i += 1
            out.append("<blockquote>" + render("\n".join(quote)) + "</blockquote>")
            continue
        para.append(line)
        i += 1
    flush_para()
    return "\n".join(out)
