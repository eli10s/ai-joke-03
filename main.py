# ai-joke-03 entry: writes one fixed one-liner about AI coding agents
# to /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output
# outside the grader's container). Deterministic: the joke is a single
# constant, so every run writes the same bytes, with no network access
# and no randomness anywhere in the program.
import os
from pathlib import Path

JOKE = "My coding agent doesn't hallucinate libraries \u2014 it just imports them from a timeline where they exist."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
