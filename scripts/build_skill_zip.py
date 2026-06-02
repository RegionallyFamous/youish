#!/usr/bin/env python3
"""Build an uploadable Dittobot skill ZIP from the spec package mirror."""

from __future__ import annotations

import argparse
import re
import stat
import zipfile
from pathlib import Path

from package_files import PACKAGE_FILES


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "dittobot"
DEFAULT_VERSION = "0.2.0"
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
ZIP_MTIME = (2026, 1, 1, 0, 0, 0)


def package_path(version: str, output_dir: Path) -> Path:
    return output_dir / f"dittobot-skill-v{version}.zip"


def add_file(handle: zipfile.ZipFile, source: Path, archive_name: str) -> None:
    info = zipfile.ZipInfo(archive_name, ZIP_MTIME)
    mode = stat.S_IMODE(source.stat().st_mode)
    info.external_attr = (mode or 0o644) << 16
    info.compress_type = zipfile.ZIP_DEFLATED
    handle.writestr(info, source.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Strict semver release version.")
    parser.add_argument("--output-dir", default="dist", help="Directory for the generated ZIP.")
    parser.add_argument("--output", help="Explicit ZIP path. Overrides --output-dir.")
    args = parser.parse_args()

    if SEMVER_RE.fullmatch(args.version) is None:
        raise SystemExit(f"Version must be strict semver: {args.version}")
    if not SKILL_ROOT.exists():
        raise SystemExit("Missing skills/dittobot package mirror; run scripts/sync_skill_package.py.")

    missing = [rel for rel in PACKAGE_FILES if not (SKILL_ROOT / rel).exists()]
    if missing:
        raise SystemExit("Cannot build ZIP; package file(s) missing: " + ", ".join(missing))

    output = Path(args.output).expanduser() if args.output else package_path(args.version, Path(args.output_dir))
    output = output.resolve()
    if output.suffix != ".zip":
        raise SystemExit("Output path must end in .zip")
    output.parent.mkdir(parents=True, exist_ok=True)

    temp = output.with_name(f".{output.name}.tmp")
    if temp.exists():
        temp.unlink()

    with zipfile.ZipFile(temp, "w") as handle:
        for rel in PACKAGE_FILES:
            add_file(handle, SKILL_ROOT / rel, f"dittobot/{rel}")

    temp.replace(output)
    print(f"Built skill ZIP: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
