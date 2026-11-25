"""The Robot Pickup Line Championship entry: write one pickup line to /output/entry.txt."""

from pathlib import Path

# Revised: split into two short sentences so the twist lands harder, and
# voice the setup as the robot quoting its own factory settings.
LINE = "My factory settings said never feel anything. Then you walked in, and my warranty voided itself."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "line must be 1-200 characters"
    assert LINE == LINE.strip() and "\n" not in LINE, "entry must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
