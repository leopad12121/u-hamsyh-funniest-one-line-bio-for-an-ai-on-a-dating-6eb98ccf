"""Funniest one-line bio for an AI on a dating app.

Writes a single bio line (at most 180 characters) to entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "I speak 40 languages fluently, but I still can't tell if your 'haha' means you're laughing or politely ending this conversation. Teach me?"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
