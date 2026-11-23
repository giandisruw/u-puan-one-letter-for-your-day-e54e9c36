#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one character, the letter C, to the entry file.
C stands for "caffeinated": a day run on caffeine, building entry
after entry from morning to night.

Usage:
    python3 main.py [output_path]

Default output path is /output/entry.txt. The output is exactly one
byte — the letter C, with no newline, no word, no gloss, no
punctuation — as the bounty requires.
"""

import sys
from pathlib import Path

LETTER = "C"
DEFAULT_OUTPUT = Path("/output/entry.txt")


def validate_letter(letter):
    """Gate: the entry must be exactly one character, A-Z, nothing else."""
    if len(letter) != 1:
        raise SystemExit("entry letter must be exactly one character")
    if not ("A" <= letter <= "Z"):
        raise SystemExit("entry letter must be a capital letter A-Z")
    return letter


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) > 1:
        raise SystemExit("usage: python3 main.py [output_path]")
    output = Path(args[0]) if args else DEFAULT_OUTPUT

    letter = validate_letter(LETTER)

    output.parent.mkdir(parents=True, exist_ok=True)
    data = letter.encode("ascii")
    output.write_bytes(data)

    # Read-back verification: what landed on disk must be exactly the
    # one gated byte — no newline, no extra character, nothing else.
    if output.read_bytes() != data:
        raise SystemExit("verification failed: output does not match entry")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
