#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry.

Writes one funny line pitching a terrible pizza topping to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""
import os
import sys

ENTRY_TEXT = (
    "Introducing the Token Crust pizza: 8,376 tokens of stale dough, "
    "because I spent my whole budget describing the topping and had "
    "nothing left for the cheese."
)
# The pitch: the agent blew its entire token budget on the topping's
# description, so the pizza itself has no cheese — self-blame in the
# final clause, token machinery turning on the agent itself.


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY_TEXT
    # In-program gate: 1-200 characters, single line, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
