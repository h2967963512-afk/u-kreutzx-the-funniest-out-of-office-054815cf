"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line of an out-of-office auto-reply: a cat has
# taken over the inbox, deleted three emails, and feels no remorse.
# One line, 135 characters — inside the 140-character gate.
# Revision note (parent pass): re-checked after the local run —
# the 135-character line is unchanged; this note only records the check.
import os

TEXT = (
    "I'm out of office until Monday. My inbox is being handled by "
    "my cat, who has deleted three of your emails already and "
    "feels no remorse."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
