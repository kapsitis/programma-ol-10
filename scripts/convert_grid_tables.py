#!/usr/bin/env python3
"""Convert Pandoc-style grid tables in a Markdown file to GitHub-friendly tables.

The script rewrites only grid-table blocks inside the file. Each detected
table block is passed through pandoc and converted to HTML with MathJax-style
math delimiters, which GitHub Pages can render reliably even when a table is
too complex to express as a plain pipe table.

Usage:
    python scripts/convert_grid_tables.py <markdown_file>
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


BORDER_RE = re.compile(r"^\+[=:\-+]+\+\s*$")
CONTENT_RE = re.compile(r"^\|.*\|\s*$")


def is_table_line(line: str) -> bool:
    return bool(BORDER_RE.match(line) or CONTENT_RE.match(line))


def convert_table(block: str) -> str:
    result = subprocess.run(
        [
            "pandoc",
            "--from",
            "markdown+grid_tables+tex_math_dollars",
            "--to",
            "html",
            "--mathjax",
            "--wrap=none",
        ],
        input=block,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True,
    )
    return result.stdout.rstrip("\n") + "\n"


def rewrite_tables(text: str) -> tuple[str, int]:
    lines = text.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    converted = 0

    while index < len(lines):
        if not BORDER_RE.match(lines[index].rstrip("\n")):
            output.append(lines[index])
            index += 1
            continue

        end = index + 1
        while end < len(lines) and is_table_line(lines[end].rstrip("\n")):
            end += 1

        block = "".join(lines[index:end])
        try:
            converted_block = convert_table(block)
        except subprocess.CalledProcessError as exc:
            raise RuntimeError(
                f"pandoc failed while converting table starting near line {index + 1}:\n{exc.stderr}"
            ) from exc

        output.append(converted_block)
        converted += 1
        index = end

    return "".join(output), converted


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/convert_grid_tables.py <markdown_file>", file=sys.stderr)
        return 1

    target = Path(sys.argv[1])
    if not target.is_file():
        print(f"Error: file not found: {target}", file=sys.stderr)
        return 1

    original = target.read_text(encoding="utf-8")
    updated, converted = rewrite_tables(original)

    if converted == 0:
        print(f"No grid tables found in {target}")
        return 0

    target.write_text(updated, encoding="utf-8", newline="\n")
    print(f"Converted {converted} grid table(s) in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())