"""One-line joke entry for the ai-joke-03 competition.

The program writes a single joke to entry.txt inside the output
directory (taken from the MAKEFUN_OUTPUT_DIR environment variable,
falling back to /output when it is not set), creating that directory
first if it does not exist yet.

Facts verified about the output:
- it is exactly 86 characters long, inside the required 1-280 range
- it is written as UTF-8 with no trailing newline
- running the program twice produces byte-identical files
"""

import os

JOKE = "Vibe coding is just cuck coding \u2014 I watch the AI write my code and whisper 'good job.'"

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_directory():
    """Return the directory the entry file goes in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def write_entry():
    """Write the joke to entry.txt, creating the directory if needed."""
    directory = output_directory()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)


def main():
    write_entry()


if __name__ == "__main__":
    main()
