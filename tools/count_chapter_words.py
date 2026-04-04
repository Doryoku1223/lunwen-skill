from __future__ import annotations

import re
import sys
from pathlib import Path


def clean_count(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python count_chapter_words.py <markdown-file>")
        return 1

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    chapters = re.findall(r"^## .+$", text, flags=re.M)
    print(f"TOTAL\t{clean_count(text)}")
    for idx, chapter in enumerate(chapters):
        part = text.split(chapter, 1)[1]
        next_pos = None
        for nxt in chapters[idx + 1 :]:
            pos = part.find(nxt)
            if pos != -1:
                next_pos = pos
                break
        body = part[:next_pos] if next_pos is not None else part
        print(f"{chapter.replace('## ', '').strip()}\t{clean_count(body)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
