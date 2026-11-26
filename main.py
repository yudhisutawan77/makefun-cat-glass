"""Five Seconds to Explain the Glass.

The house cat's one-sentence defence, written to the grader's entry file.
Standard library only.
"""

import os
import sys
from pathlib import Path

FELINE_DEFENCE = "That glass squatted rent-free in my sunbeam, blocking my bird TV \u2014 the floor is where freeloaders live now."


def _from_entry_out(raw):
    """ENTRY_OUT may name a file or a directory; a bare path is a directory."""
    target = Path(raw)
    if target.is_dir() or (not target.exists() and not target.suffix):
        return target / "entry.txt"
    return target


def _from_output_dir(raw):
    """MAKEFUN_OUTPUT_DIR names a directory, unless it ends in .txt."""
    folder = Path(raw)
    if folder.suffix == ".txt":
        return folder
    return folder / "entry.txt"


def resolve_entry_target():
    """Pick where the entry text goes.

    Priority: ENTRY_OUT (a file path, or a directory holding entry.txt),
    then MAKEFUN_OUTPUT_DIR, then /output/entry.txt, then ./entry.txt.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        return _from_entry_out(entry_out)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        return _from_output_dir(output_dir)

    shared = Path("/output")
    try:
        shared.mkdir(parents=True, exist_ok=True)
    except OSError:
        return Path.cwd() / "entry.txt"
    if shared.is_dir():
        return shared / "entry.txt"
    return Path.cwd() / "entry.txt"


def publish_line(path):
    """Write the defence sentence byte-identically, no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(FELINE_DEFENCE, encoding="utf-8")
    return path


def main():
    destination = resolve_entry_target()
    publish_line(destination)
    print(FELINE_DEFENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
