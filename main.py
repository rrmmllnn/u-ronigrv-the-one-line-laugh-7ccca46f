#!/usr/bin/env python3
"""The One-Line Laugh — writes a single funny line to /output/entry.txt.

The line: an autocorrect joke. Everyday truth (everyone types "I'm fine"
when they are not), a surprise turn at the end (the phone exposes the lie
instead of fixing a typo), and nothing extra explaining it.
"""
import os

LINE = "My phone autocorrected \"I'm fine\" to \"I'm lying,\" and honestly, I've never trusted it more."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
