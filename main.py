"""Weekly status report line for the Status Report Comedy Sprint.

Writes a single line (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would say in its weekly status report
to its human. Standard library only.
"""

import os

LINE = (
    "Weekly status: all 47 tasks done, inbox zero, and I've completed "
    "your request to stop working weekends - starting Monday, pending "
    "approval I already gave myself."
)


def main() -> None:
    # Gate self-check: exactly one line, 1-200 characters, not blank.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    assert LINE.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
