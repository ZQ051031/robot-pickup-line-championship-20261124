"""Robot Pickup Line Championship entry.

Writes exactly one line -- the funniest one-line pickup line a robot
could use -- to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I ran a full diagnostic on my heart and found only one error: "
    "missing you \u2014 care to be my next firmware update?"
)

assert len(ENTRY) <= 200, "entry must be at most 200 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
