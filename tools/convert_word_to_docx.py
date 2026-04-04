from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


def convert_with_word(source: Path, target: Path) -> bool:
    try:
        import win32com.client  # type: ignore
    except Exception:
        return False

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    doc = None
    try:
        doc = word.Documents.Open(str(source.resolve()))
        doc.SaveAs(str(target.resolve()), FileFormat=16)
        return True
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()


def convert_with_soffice(source: Path, target: Path) -> bool:
    soffice = shutil.which("soffice")
    if not soffice:
        return False
    temp_dir = target.parent.resolve()
    cmd = [
        soffice,
        "--headless",
        "--convert-to",
        "docx",
        "--outdir",
        str(temp_dir),
        str(source.resolve()),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return False
    converted = temp_dir / f"{source.stem}.docx"
    if not converted.exists():
        return False
    if converted.resolve() != target.resolve():
        if target.exists():
            target.unlink()
        converted.replace(target)
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python convert_word_to_docx.py <source.doc|source.docx> [target.docx]")
        return 1

    source = Path(sys.argv[1])
    if not source.exists():
        print(f"Source not found: {source}", file=sys.stderr)
        return 2

    target = Path(sys.argv[2]) if len(sys.argv) >= 3 else source.with_suffix(".docx")
    target.parent.mkdir(parents=True, exist_ok=True)

    if source.suffix.lower() == ".docx":
        if source.resolve() != target.resolve():
            shutil.copy2(source, target)
        print(target)
        return 0

    if source.suffix.lower() != ".doc":
        print(f"Unsupported suffix: {source.suffix}", file=sys.stderr)
        return 3

    if convert_with_word(source, target) or convert_with_soffice(source, target):
        print(target)
        return 0

    print(
        "Unable to convert .doc to .docx. Install Microsoft Word with pywin32 or LibreOffice soffice.",
        file=sys.stderr,
    )
    return 4


if __name__ == "__main__":
    raise SystemExit(main())
