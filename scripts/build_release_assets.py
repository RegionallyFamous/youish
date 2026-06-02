#!/usr/bin/env python3
"""Build and verify all local Dittobot release assets in one command."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from package_files import assert_mirror_fresh
from plugin_manifest import DEFAULT_VERSION, require_semver


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str], *, stdout=None) -> None:
    display = " ".join(str(arg) for arg in args)
    print(f"+ {display}", flush=True)
    result = subprocess.run(args, cwd=ROOT, stdout=stdout, check=False)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def assert_safe_release_dir(path: Path) -> None:
    dist = (ROOT / "dist").resolve()
    resolved = path.resolve()
    if resolved == dist:
        raise SystemExit("Refusing to use dist itself as the release directory.")
    if dist not in resolved.parents:
        raise SystemExit("Release directory must live under dist/.")
    if not resolved.name.startswith("release-v"):
        raise SystemExit("Release directory name must start with release-v.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Strict semver release version.")
    parser.add_argument(
        "--output-dir",
        help="Release asset directory. Defaults to dist/release-vVERSION.",
    )
    args = parser.parse_args()

    require_semver(args.version)
    release_dir = (
        Path(args.output_dir).expanduser()
        if args.output_dir
        else ROOT / "dist" / f"release-v{args.version}"
    ).resolve()
    assert_safe_release_dir(release_dir)

    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir(parents=True, exist_ok=True)
    work_dir = release_dir / "_work"
    plugin_dir = work_dir / "dittobot-plugin"
    work_dir.mkdir()

    run([sys.executable, "scripts/sync_skill_package.py"])
    assert_mirror_fresh(ROOT)
    run([sys.executable, "scripts/validate_skill.py"])
    run([sys.executable, "scripts/regression_100.py"])
    run(
        [
            sys.executable,
            "scripts/build_plugin.py",
            "--output-dir",
            str(plugin_dir),
            "--version",
            args.version,
        ]
    )
    run(
        [
            sys.executable,
            "scripts/check_plugin_package.py",
            str(plugin_dir),
            "--version",
            args.version,
        ]
    )
    run(
        [
            sys.executable,
            "scripts/build_skill_zip.py",
            "--version",
            args.version,
            "--output-dir",
            str(release_dir),
        ]
    )
    skill_zip = release_dir / f"dittobot-skill-v{args.version}.zip"
    run([sys.executable, "scripts/check_skill_zip.py", str(skill_zip)])
    run(
        [
            sys.executable,
            "scripts/build_plugin_zip.py",
            str(plugin_dir),
            "--version",
            args.version,
            "--output-dir",
            str(release_dir),
        ]
    )
    plugin_zip = release_dir / f"dittobot-plugin-v{args.version}.zip"
    run(
        [
            sys.executable,
            "scripts/check_plugin_zip.py",
            str(plugin_zip),
            "--version",
            args.version,
        ]
    )
    scorecard = release_dir / f"dittobot-scorecard-v{args.version}.json"
    with scorecard.open("w", encoding="utf-8") as handle:
        run(
            [
                sys.executable,
                "scripts/scorecard.py",
                "--plugin-dir",
                str(plugin_dir),
                "--version",
                args.version,
                "--format",
                "json",
            ],
            stdout=handle,
        )
    run(
        [
            sys.executable,
            "scripts/write_checksums.py",
            str(skill_zip),
            str(plugin_zip),
            str(scorecard),
            "--output",
            str(release_dir / "SHA256SUMS"),
        ]
    )
    run(
        [
            sys.executable,
            "scripts/check_release_assets.py",
            str(release_dir),
            "--version",
            args.version,
        ]
    )
    shutil.rmtree(work_dir)

    print()
    print(f"Release assets are ready in {release_dir}:")
    for name in sorted(path.name for path in release_dir.iterdir() if path.is_file()):
        print(f"  {name}")
    print()
    print("Create the GitHub release after tagging the validated commit:")
    print(
        "  gh release create v{0} "
        "dist/release-v{0}/dittobot-skill-v{0}.zip "
        "dist/release-v{0}/dittobot-plugin-v{0}.zip "
        "dist/release-v{0}/dittobot-scorecard-v{0}.json "
        "dist/release-v{0}/SHA256SUMS "
        "--verify-tag --fail-on-no-commits "
        '--title "Dittobot v{0}" --generate-notes'.format(args.version)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
