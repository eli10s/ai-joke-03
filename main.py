# ai-joke-03 entry: writes one fixed one-liner about AI coding agents
# to /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output
# outside the grader's container). Deterministic: the joke is a single
# constant, so every run writes the same bytes, with no network access
# and no randomness anywhere in the program.
# Verified 2026-11-13: the joke is 86 characters (within the 1-280 limit),
# and two local runs wrote byte-identical output (entry.txt, 88 bytes UTF-8).
import os
from pathlib import Path

JOKE = "Vibe coding is just cuck coding \u2014 I watch the AI write my code and whisper 'good job.'"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
