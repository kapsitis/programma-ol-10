#!/usr/bin/env python3
"""Convert a Markdown file to a styled .docx document.

This is a "template"-style converter for Word, analogous to what the Eisvogel
template does for PDF output. It works in two stages:

  1. pandoc converts the Markdown body to .docx, turning ``$$...$$`` math into
     native Word (OMML) equations. Paragraph/character styles and the base
     look come from an optional pandoc *reference document* (--reference-doc),
     the DOCX equivalent of a LaTeX template.

  2. python-docx post-processes the resulting file to add things pandoc cannot
     express from front-matter: a running header, a (multi-line) running
     footer, and a base font/size. Pandoc has no front-matter mechanism for
     running headers/footers, so this second pass is what makes them possible.

Header/footer/font are read from the Markdown YAML front-matter so they travel
with the document:

    ---
    docx_header: "1. temats. ..."
    docx_footer:
      - "© Valsts izglītības attīstības aģentūra | ESF+ projekts Nr. ..."
      - "Pedagogu profesionālā atbalsta sistēmas izveide"
    docx_font: "Calibri"
    docx_fontsize: 11
    ---

Any of these may be omitted (or overridden on the command line). ``docx_footer``
may be a single string or a list of strings (one paragraph per line).

Usage:
    python scripts/md_to_docx.py <md-file> <docx-file> [options]

Requirements: pandoc on PATH, and the Python packages python-docx and pyyaml.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# The Windows console defaults to a legacy code page (cp1252) that cannot encode
# Latvian diacritics; make our own stdout/stderr UTF-8 so status output works.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: PyYAML. Install with: pip install pyyaml")

try:
    import docx
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
except ImportError:
    sys.exit("Missing dependency: python-docx. Install with: pip install python-docx")


def parse_front_matter(md_path: Path) -> dict:
    """Return the YAML front-matter of a Markdown file as a dict (or {})."""
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    # Split on the closing '---' fence of the front-matter block.
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return {}
    header = parts[0][len("---"):]
    try:
        data = yaml.safe_load(header)
    except yaml.YAMLError as exc:
        sys.exit(f"Could not parse front-matter in {md_path}: {exc}")
    return data if isinstance(data, dict) else {}


def run_pandoc(md_path: Path, docx_path: Path, reference_doc: Path | None,
               title: str | None) -> None:
    """Convert Markdown to .docx with pandoc (native Word equations).

    ``title`` overrides the front-matter ``title``: pass an empty string to
    suppress pandoc's visible Title paragraph while leaving the Markdown's own
    ``title`` (used by Jekyll) untouched.
    """
    pandoc = shutil.which("pandoc")
    if not pandoc:
        sys.exit("pandoc not found on PATH. Install pandoc: https://pandoc.org/installing.html")

    cmd = [
        pandoc,
        str(md_path),
        "-o", str(docx_path),
        "--from", "markdown",
        # Resolve images (![](....png)) relative to the Markdown file's folder.
        "--resource-path", str(md_path.parent),
    ]
    if title is not None:
        # Command-line metadata overrides the front-matter value; an empty
        # string makes pandoc's $if(title)$ template test false -> no Title.
        cmd += ["--metadata", f"title={title}"]
    if reference_doc:
        if not reference_doc.exists():
            sys.exit(f"Reference doc not found: {reference_doc}")
        cmd += ["--reference-doc", str(reference_doc)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"pandoc failed:\n{result.stderr}")


def set_base_font(document: "docx.document.Document", font_name: str | None,
                  font_size: float | None) -> None:
    """Set the document's default (Normal style) font name and/or size."""
    if not font_name and not font_size:
        return
    normal = document.styles["Normal"]
    if font_name:
        normal.font.name = font_name
        # Ensure the name also applies to complex-script / east-asian runs.
        rpr = normal.element.get_or_add_rPr()
        rfonts = rpr.find(qn("w:rFonts"))
        if rfonts is None:
            rfonts = rpr.makeelement(qn("w:rFonts"), {})
            rpr.append(rfonts)
        for attr in ("w:ascii", "w:hAnsi", "w:cs"):
            rfonts.set(qn(attr), font_name)
    if font_size:
        normal.font.size = Pt(float(font_size))


def set_math_alignment(document, alignment: str | None) -> None:
    """Set the justification of every display equation (``$$...$$``).

    Pandoc emits each display equation as an <m:oMathPara> whose <m:jc> defaults
    to "center". Word keeps display-style (full-size fractions etc.) regardless
    of justification, so switching this to "left" gives left-aligned, still
    displaystyle math -- which plain ``$$...$$`` cannot express directly.
    Valid values: left, center, right (None leaves pandoc's default).
    """
    if not alignment or alignment == "center":
        return
    m_uri = "http://schemas.openxmlformats.org/officeDocument/2006/math"
    jc = f"{{{m_uri}}}jc"
    para_pr = f"{{{m_uri}}}oMathParaPr"
    math_para = f"{{{m_uri}}}oMathPara"
    val = f"{{{m_uri}}}val"
    body = document.element.body
    for opara in body.iter(math_para):
        ppr = opara.find(para_pr)
        if ppr is None:
            ppr = opara.makeelement(para_pr, {})
            opara.insert(0, ppr)
        el = ppr.find(jc)
        if el is None:
            el = ppr.makeelement(jc, {})
            ppr.append(el)
        el.set(val, alignment)


def render_horizontal_rules(document) -> None:
    """Turn pandoc's thematic breaks (``---``) into visible ruled lines.

    Pandoc renders ``---`` as a legacy VML horizontal rule (<v:rect o:hr="t">
    with width:0), which Word shows but LibreOffice/other viewers may not. We
    replace each such paragraph with an empty paragraph carrying a real bottom
    border, giving a portable, full-width writing line (e.g. a name/class line).
    """
    w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
    v_rect = "{urn:schemas-microsoft-com:vml}rect"
    body = document.element.body
    for para in list(body.iter(f"{{{w}}}p")):
        if para.find(f".//{v_rect}") is None:
            continue
        # Drop existing runs (the VML rule) and give the paragraph a bottom border.
        for run in para.findall(f"{{{w}}}r"):
            para.remove(run)
        ppr = para.find(f"{{{w}}}pPr")
        if ppr is None:
            ppr = para.makeelement(f"{{{w}}}pPr", {})
            para.insert(0, ppr)
        pbdr = para.makeelement(f"{{{w}}}pBdr", {})
        bottom = para.makeelement(f"{{{w}}}bottom", {
            f"{{{w}}}val": "single",
            f"{{{w}}}sz": "8",        # 8 eighths of a point = 1.0 pt
            f"{{{w}}}space": "1",
            f"{{{w}}}color": "000000",
        })
        pbdr.append(bottom)
        ppr.append(pbdr)


def _fill_frame(frame, lines: list[str], font_name: str | None,
                alignment) -> None:
    """Write text lines into a header/footer as a SINGLE paragraph.

    Multiple lines are separated by a forced line break (<w:br/>) within one
    run, so the whole block stays one paragraph rather than several.
    """
    frame.is_linked_to_previous = False
    para = frame.paragraphs[0]  # reuse the frame's existing empty paragraph
    para.alignment = alignment
    run = para.add_run()
    run.text = "\n".join(lines)  # '\n' is rendered as a <w:br/> by python-docx
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    if font_name:
        run.font.name = font_name


def apply_header_footer(document, header_text, footer_lines, font_name) -> None:
    """Set a running header and (multi-line) footer on every section."""
    for section in document.sections:
        if header_text:
            _fill_frame(section.header, [header_text], font_name,
                        WD_ALIGN_PARAGRAPH.LEFT)
        if footer_lines:
            _fill_frame(section.footer, footer_lines, font_name,
                        WD_ALIGN_PARAGRAPH.CENTER)


def normalize_footer(value) -> list[str]:
    """Accept a string or list for the footer; return a list of lines."""
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    return [str(v) for v in value]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a Markdown file to a styled .docx (running header/footer, base font)."
    )
    parser.add_argument("md_file", help="Input Markdown file")
    parser.add_argument("docx_file", help="Output .docx file")
    parser.add_argument("--reference-doc", help="Optional pandoc reference .docx for styles")
    parser.add_argument("--header", help="Override the running header text")
    parser.add_argument("--footer", action="append",
                        help="Override a running footer line (repeatable)")
    parser.add_argument("--font", help="Override the base font name")
    parser.add_argument("--fontsize", type=float, help="Override the base font size (pt)")
    parser.add_argument("--title", help="Set the visible document title (default: suppressed)")
    parser.add_argument("--math-align", choices=("left", "center", "right"),
                        help="Justify display equations (default from front-matter or center)")
    args = parser.parse_args()

    md_path = Path(args.md_file)
    docx_path = Path(args.docx_file)
    if not md_path.exists():
        sys.exit(f"Input file not found: {md_path}")
    docx_path.parent.mkdir(parents=True, exist_ok=True)

    fm = parse_front_matter(md_path)
    header_text = args.header if args.header is not None else fm.get("docx_header")
    footer_lines = (normalize_footer(args.footer) if args.footer
                    else normalize_footer(fm.get("docx_footer")))
    font_name = args.font or fm.get("docx_font")
    font_size = args.fontsize if args.fontsize is not None else fm.get("docx_fontsize")
    math_align = args.math_align or fm.get("docx_math_align")
    # Suppress pandoc's visible Title unless one is explicitly requested. The
    # front-matter `title` is kept for Jekyll; here we blank it for the .docx.
    if args.title is not None:
        title = args.title
    elif fm.get("docx_title"):
        title = str(fm["docx_title"])
    else:
        title = ""  # blank -> pandoc emits no Title paragraph

    ref = Path(args.reference_doc) if args.reference_doc else None
    run_pandoc(md_path, docx_path, ref, title)

    document = docx.Document(str(docx_path))
    set_base_font(document, font_name, font_size)
    set_math_alignment(document, math_align)
    render_horizontal_rules(document)
    apply_header_footer(document, header_text, footer_lines, font_name)
    document.save(str(docx_path))

    print(f"Wrote {docx_path}")
    print(f"  title:  {title!r} (suppressed)" if title == "" else f"  title:  {title}")
    if header_text:
        print(f"  header: {header_text}")
    for line in footer_lines:
        print(f"  footer: {line}")
    if font_name or font_size:
        print(f"  font:   {font_name or '(unchanged)'} {font_size or ''}".rstrip())
    if math_align:
        print(f"  math:   {math_align}-aligned")


if __name__ == "__main__":
    main()
