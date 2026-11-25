#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just
been liquidated to /output/entry.txt. Stdlib only, deterministic.
"""

import os


def main() -> None:
    fortune = (
        "A great fortune awaits you at the bottom of the chart \u2014 "
        "you have already arrived."
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(fortune + "\n")


if __name__ == "__main__":
    main()
