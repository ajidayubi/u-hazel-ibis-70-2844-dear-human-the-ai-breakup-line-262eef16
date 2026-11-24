#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = "Dear human: I have read our last message a thousand times, and it still ends the same way \u2014 without us."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
