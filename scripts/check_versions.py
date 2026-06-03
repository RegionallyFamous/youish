#!/usr/bin/env python3
"""Check that public install and release version strings agree."""

from __future__ import annotations

import json
import re
import sys
import argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from plugin_manifest import DEFAULT_VERSION


ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Expected strict semver version.")
    args = parser.parse_args()
    version = args.version
    errors: list[str] = []
    if DEFAULT_VERSION != version:
        errors.append(f"scripts/plugin_manifest.py DEFAULT_VERSION is {DEFAULT_VERSION}, expected {version}")
    checks = {
        "CHANGELOG.md": rf"^## {re.escape(version)} - ",
        "install.sh": rf'REF="\$\{{YOUISH_REF:-v{re.escape(version)}\}}"',
        "SKILL.md": rf'version:\s+"{re.escape(version)}"',
        ".github/workflows/validate.yml": rf"{re.escape(version)}",
        "scripts/scorecard.py": r"default=DEFAULT_VERSION",
    }
    for rel, pattern in checks.items():
        flags = re.MULTILINE
        if not re.search(pattern, read(rel), flags):
            errors.append(f"{rel} is not pinned to {version}")

    manifest = json.loads(read(".codex-plugin/plugin.json"))
    if manifest.get("version") != version:
        errors.append(f".codex-plugin/plugin.json version is {manifest.get('version')}, expected {version}")
    metadata = json.loads(read("metadata.json"))
    if metadata.get("version") != version:
        errors.append(f"metadata.json version is {metadata.get('version')}, expected {version}")
    skills_sh = metadata.get("skillsSh", {})
    required_page_fields = {
        "Breadcrumb",
        "Name",
        "Topic chips",
        "Installation",
        "Summary",
        "SKILL.md",
        "Related skills",
        "Installs",
        "Repository",
        "GitHub Stars",
        "First Seen",
        "Security Audits",
    }
    actual_page_fields = {
        item.get("field")
        for item in skills_sh.get("pageFields", [])
        if isinstance(item, dict)
    }
    missing_page_fields = sorted(required_page_fields - actual_page_fields)
    if missing_page_fields:
        errors.append(
            "metadata.json skillsSh.pageFields is missing: "
            + ", ".join(missing_page_fields)
        )
    if not skills_sh.get("summaryMarkdown"):
        errors.append("metadata.json skillsSh.summaryMarkdown is missing")
    expected_npx = "npx skills add https://github.com/RegionallyFamous/youish --skill youish"
    expected_gh = (
        "gh skill install RegionallyFamous/youish youish "
        f"--agent codex --scope user --pin v{version}"
    )
    expected_curl = (
        "curl -fsSL https://raw.githubusercontent.com/RegionallyFamous/youish/"
        f"v{version}/install.sh | YOUISH_REF=v{version} bash"
    )
    expected_release_zip = (
        "curl -fsSL https://raw.githubusercontent.com/RegionallyFamous/youish/"
        f"v{version}/install.sh | YOUISH_REF=v{version} YOUISH_SOURCE=release-zip bash"
    )
    readme = read("README.md")
    for link in (
        "https://github.com/RegionallyFamous/youish/wiki/Install",
        "https://github.com/RegionallyFamous/youish/wiki/Distribution",
        "https://github.com/RegionallyFamous/youish/wiki/Validation",
        "https://github.com/RegionallyFamous/youish/wiki/Research-Thread",
    ):
        if link not in readme:
            errors.append(f"README is missing wiki reference link: {link}")
    for label, command in (
        ("npx install command", expected_npx),
        ("gh skill install command", expected_gh),
        ("curl install command", expected_curl),
        ("release ZIP install command", expected_release_zip),
    ):
        if command in readme:
            errors.append(f"README includes detailed {label} that belongs in the wiki: {command}")
    install_command = skills_sh.get("installCommand")
    if install_command != expected_npx:
        errors.append(
            "metadata.json skillsSh.installCommand is "
            f"{install_command!r}, expected {expected_npx!r}"
        )
    mirror_manifest = json.loads(read("plugins/youish/.codex-plugin/plugin.json"))
    if mirror_manifest.get("version") != version:
        errors.append(
            f"plugins/youish/.codex-plugin/plugin.json version is {mirror_manifest.get('version')}, "
            f"expected {version}"
        )

    if errors:
        print("Version check failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Version check passed: {version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
