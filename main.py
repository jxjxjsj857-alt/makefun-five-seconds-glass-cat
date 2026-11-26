#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.
"""

import os

ENTRY = (
    "That glass kept showing a stranger cat in my house, so I evicted it, "
    "and the floor was simply the fastest way out."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if text != ENTRY:
        raise SystemExit("entry must not carry leading or trailing whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
