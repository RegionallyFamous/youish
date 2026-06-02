#!/usr/bin/env python3
"""Write SHA256 checksums for release assets."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assets", nargs="+", help="Release asset files to hash.")
    parser.add_argument("--output", default="dist/SHA256SUMS", help="Checksum file path.")
    args = parser.parse_args()

    assets = [Path(asset).expanduser().resolve() for asset in args.assets]
    missing = [str(path) for path in assets if not path.is_file()]
    if missing:
        raise SystemExit("Cannot checksum missing asset(s): " + ", ".join(missing))
    names = [path.name for path in assets]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SystemExit("Cannot checksum assets with duplicate basename(s): " + ", ".join(duplicates))

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{digest(path)}  {path.name}" for path in sorted(assets)]
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote checksums: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
