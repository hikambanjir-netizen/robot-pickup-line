#!/usr/bin/env python3
"""Print one robot pickup line, exactly one line, 1-200 chars."""
import sys

LINE = "I ran a full system scan for the best use of my battery \u2014 every sensor pointed at you, so here I am, overheating."

def main():
    # Gate: exactly one line, non-blank, 1-200 characters, no hidden newlines.
    if "\n" in LINE or "\r" in LINE or LINE != LINE.strip() or not 1 <= len(LINE) <= 200:
        print(f"error: pickup line must be exactly 1 line, 1-200 characters (got {len(LINE)})", file=sys.stderr)
        return 1
    print(LINE)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
