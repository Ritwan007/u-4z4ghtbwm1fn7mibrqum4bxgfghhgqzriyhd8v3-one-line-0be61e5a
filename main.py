#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line to /output/entry.txt.
"""

import os

# The joke is built from two named parts so each half can be read and
# tweaked on its own; joining them keeps the line exactly as written.
SETUP = "I told my AI assistant to act more human; "
PUNCHLINE = "now it replies 'per my last email' and I can't fire it."

LINE = SETUP + PUNCHLINE


def validate_entry(text):
    """Guard: the competition gate is 1-140 chars, one line, non-blank."""
    if not 1 <= len(text) <= 140:
        raise SystemExit("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main():
    text = LINE
    validate_entry(text)
    encoded = text.encode("utf-8")  # raises if not valid UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
