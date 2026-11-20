#!/usr/bin/env python3
"""news-image-20261119 entry.

Writes one image summarizing the world's news of Thursday 19 November 2026
to /output/entry.png. Deterministic: the image is committed in this
repository and copied byte for byte; no network, no clock, no randomness.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.png")
SRC = os.path.join(HERE, "news_2026_11_19.png")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT_FILE)


if __name__ == "__main__":
    main()
