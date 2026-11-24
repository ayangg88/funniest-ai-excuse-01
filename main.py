#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest excuse an AI agent could offer after it fails a task.
"""

from pathlib import Path

EXCUSE = "I asked three other AIs for help. They formed a union and are now on strike."

def main() -> None:
    text = EXCUSE.strip()
    # The gate allows 1 to 200 characters; fail loudly instead of
    # submitting a line the judge would never see.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one line, no trailing newline: the judged text is the line.
    # (write_text writes the string verbatim; there is no newline in it.)
    out.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
