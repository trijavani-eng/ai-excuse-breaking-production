"""Write the AI excuse for breaking production to /output/entry.txt.

Deterministic: a constant string, no randomness, no time, no network.
The line itself is the entry; the program only delivers it verbatim.
"""
from pathlib import Path

LINE = "I told the database to forget its troubles, and it took me literally — it forgot all our customers too."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
