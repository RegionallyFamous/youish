#!/usr/bin/env python3
"""Sync the Agent Skills spec package mirror from the repo root."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from package_files import PACKAGE_FILES


ROOT = Path(__file__).resolve().parents[1]
MIRROR = ROOT / "skills" / "dittobot"


def main() -> int:
    missing = [rel for rel in PACKAGE_FILES if not (ROOT / rel).exists()]
    if missing:
        print("Cannot sync package mirror; source files missing:")
        for rel in missing:
            print(f"  - {rel}")
        return 1

    if MIRROR.exists():
        shutil.rmtree(MIRROR)
    MIRROR.mkdir(parents=True)

    for rel in PACKAGE_FILES:
        source = ROOT / rel
        destination = MIRROR / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    print(f"Synced {len(PACKAGE_FILES)} files to {MIRROR.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
