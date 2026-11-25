#!/usr/bin/env python3
"""Write exactly one word describing the entrant's Wi-Fi to
/output/entry.txt.

Entry for make.fun bounty "One Word for Your Wi-Fi"
(u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).
Pure standard library, no network, deterministic.
"""

import os

# The bounty gate: /output/entry.txt must hold exactly one word, 1-20
# characters, no spaces. Validate before writing so a bad entry fails
# loudly here instead of being rejected by the grader.
MAX_CHARS = 20

WORD = "Moody"


def main() -> None:
    word = WORD.strip()
    if not word:
        raise ValueError("entry is empty")
    if " " in word:
        raise ValueError("entry must be a single word with no spaces")
    if len(word) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(word)} chars, over the {MAX_CHARS} limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word + "\n")


if __name__ == "__main__":
    main()
