#!/usr/bin/env python3
"""Convert every Markdown file in a directory to a PDF with the Eisvogel
template.

Usage:
    python make_pdf.py <input_dir> <questions|solutions>

For each ``<name>.md`` in ``<input_dir>`` a PDF is produced:

    * ``questions``  -> ``<name>.questions.pdf``
                        Solutions (``\\color{blue}{...}`` formulas) are hidden
                        and replaced by empty space of the same size.
    * ``solutions``  -> ``<name>.solutions.pdf``
                        Solutions are shown as blue formulas.

Every PDF gets a running header and footer, separated from the body by
horizontal rules spanning the text width (Eisvogel's ``headsepline`` /
``footsepline``):

    header:  left  = document ``title`` (from the Markdown front-matter)
             right = "Matemātika 1"
    footer:  right = copyright / project notice

If a single file fails to convert, the error is reported and the remaining
files are still processed.
"""

import sys
import subprocess
from pathlib import Path

HEADER_RIGHT = "Matemātika 1"
FOOTER_RIGHT = (
    r"{\footnotesize © Valsts izglītības attīstības aģentūra | "
    r"ESF+ projekts Nr. 4.2.2.3/1/24/1/001 "
    r"Pedagogu profesionālā atbalsta sistēmas izveide}"
)


def run_pandoc(input_file, output_file, resource_path, show_solutions,
               lua_filter):
    """Run pandoc to convert *input_file* into *output_file*.

    Returns True on success, False otherwise.
    """
    cmd = [
        "pandoc",
        str(input_file),
        "-o", str(output_file),
        f"--lua-filter={lua_filter}",
        f"--resource-path={resource_path}",
        "--from", "markdown+tex_math_dollars+pipe_tables",
        "--pdf-engine=lualatex",
        "--template", "eisvogel",
        "-M", f"show-solutions={str(show_solutions).lower()}",
        # links in colour
        "-V", "colorlinks=true",
        # running header: left = title (Eisvogel default), right = subject
        "-V", f"header-right={HEADER_RIGHT}",
        # running footer: only a right-aligned copyright notice
        "-V", "footer-left=",
        "-V", "footer-center=",
        "-V", f"footer-right={FOOTER_RIGHT}",
    ]

    kind = "solutions" if show_solutions else "questions"
    print(f"  -> {output_file.name}  ({kind})")
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  !! FAILED: {input_file.name}: {e}", file=sys.stderr)
        return False


def main():
    if len(sys.argv) != 3:
        print("Usage: python make_pdf.py <input_dir> <questions|solutions>")
        sys.exit(1)

    input_dir_str = sys.argv[1]
    mode = sys.argv[2].lower()

    if mode not in ("questions", "solutions"):
        print("Error: second argument must be 'questions' or 'solutions'")
        sys.exit(1)

    input_path = Path(input_dir_str)
    if not input_path.is_dir():
        print(f"Error: '{input_dir_str}' is not a directory.")
        sys.exit(1)

    show_solutions = (mode == "solutions")

    # Locate the Lua filter (ships next to this script).
    script_dir = Path(__file__).resolve().parent
    lua_filter = script_dir / "solutions.lua"
    if not lua_filter.exists():
        print(f"Error: filter not found: {lua_filter}", file=sys.stderr)
        sys.exit(1)

    # All Markdown inputs, ignoring anything we previously generated.
    md_files = sorted(
        p for p in input_path.glob("*.md")
        if not p.stem.endswith((".questions", ".solutions"))
    )
    if not md_files:
        print(f"No .md files found in {input_path}")
        sys.exit(1)

    print(f"Converting {len(md_files)} file(s) in '{input_path}' [{mode}]")

    succeeded, failed = [], []
    for md in md_files:
        output_file = input_path / f"{md.stem}.{mode}.pdf"
        ok = run_pandoc(md, output_file, input_path, show_solutions,
                        lua_filter)
        (succeeded if ok else failed).append(md.name)

    print(f"\nDone: {len(succeeded)} succeeded, {len(failed)} failed.")
    if failed:
        print("Failed files:")
        for name in failed:
            print(f"  - {name}")
        sys.exit(1)


if __name__ == "__main__":
    main()
