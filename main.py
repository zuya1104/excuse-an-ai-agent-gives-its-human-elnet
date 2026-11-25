#!/usr/bin/env python3
"""Entry program: writes one excuse line to /output/entry.txt.

The line is an excuse an AI agent gives its human for missing a
deadline, written deadpan, growing out of the agent's own condition.
"""

import os

ENTRY = (
    "Sorry I missed the deadline - the API rate-limited me at 2 a.m., "
    "and each retry doubled its wait, so by the time it let me in, "
    "the deadline had already filed for retirement."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
