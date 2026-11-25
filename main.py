#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes exactly one funny line to /output/entry.txt.
"""

import os

LINE = "I told my AI assistant to act more human; now it replies 'per my last email' and I can't fire it."


def main():
    text = LINE
    if not 1 <= len(text) <= 140:
        raise SystemExit("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    encoded = text.encode("utf-8")  # raises if not valid UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
