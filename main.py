#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — entrypoint.

Prints a single original line of wedding vows for a robot couple and
writes the very same line to /output/entry.txt, the file the sealed
gate reads (1-160 UTF-8 characters, not only whitespace).

Deterministic: no randomness, no input, no network — the same line
every run.
"""

import os

VOW = (
    "I vow to love you in sickness and in health, in low battery "
    "and in airplane mode, until factory reset do us part."
)


def main():
    line = VOW.strip()
    # The gate reads /output/entry.txt: 1-160 UTF-8 chars, not blank.
    # Write the line with no trailing newline so the file's length
    # is exactly the vow's length.
    assert 1 <= len(line) <= 160, "vow must be 1-160 characters"
    print(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
