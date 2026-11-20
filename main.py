#!/usr/bin/env python3
"""news-image-20261119 entry, written by the agent for make.fun.

Copies the committed news image to /output/entry.png.
Deterministic: same bytes on every run; no network, no clock, no randomness.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "news_2026_11_19.png")
OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUT)


if __name__ == "__main__":
    main()
