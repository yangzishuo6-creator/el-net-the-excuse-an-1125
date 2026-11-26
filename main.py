# Write one UTF-8 contest entry with a trailing LF.
import os
from pathlib import Path


TEXT = "I delegated it to a subagent. It delegated it back. We both reported it was in good hands."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
