#!/usr/bin/env bash
set -euo pipefail

REPO="${DITTOBOT_REPO:-RegionallyFamous/dittobot}"
REF="${DITTOBOT_REF:-main}"

if [ -n "${DITTOBOT_ARCHIVE_URL:-}" ]; then
  ARCHIVE_URL="$DITTOBOT_ARCHIVE_URL"
elif [[ "$REF" == refs/* ]]; then
  ARCHIVE_URL="https://github.com/${REPO}/archive/${REF}.tar.gz"
elif [[ "$REF" == v[0-9]* ]]; then
  ARCHIVE_URL="https://github.com/${REPO}/archive/refs/tags/${REF}.tar.gz"
else
  ARCHIVE_URL="https://github.com/${REPO}/archive/refs/heads/${REF}.tar.gz"
fi

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    printf 'Dittobot needs %s. Install it, then rerun this command.\n' "$1" >&2
    exit 1
  fi
}

need curl
need tar
need python3

tmpdir="$(mktemp -d "${TMPDIR:-/tmp}/dittobot-install.XXXXXX")"
cleanup() {
  rm -rf "$tmpdir"
}
trap cleanup EXIT

archive="$tmpdir/dittobot.tar.gz"
printf 'Downloading Dittobot from %s\n' "$ARCHIVE_URL"
curl -fsSL "$ARCHIVE_URL" -o "$archive"
tar -xzf "$archive" -C "$tmpdir"

repo_dir=""
repo_count=0
for candidate in "$tmpdir"/*; do
  if [ -d "$candidate" ]; then
    repo_dir="$candidate"
    repo_count=$((repo_count + 1))
  fi
done

if [ "$repo_count" -ne 1 ]; then
  printf 'Expected exactly one Dittobot folder in the downloaded archive; found %s.\n' "$repo_count" >&2
  exit 1
fi

if [ ! -f "$repo_dir/SKILL.md" ] || ! grep -q '^name: dittobot$' "$repo_dir/SKILL.md"; then
  printf 'Downloaded archive does not look like the Dittobot skill repo.\n' >&2
  exit 1
fi

if [ ! -f "$repo_dir/scripts/install.py" ]; then
  printf 'Could not find scripts/install.py in the Dittobot archive.\n' >&2
  exit 1
fi

printf 'Installing Dittobot into the Codex user skills folder...\n'
python3 "$repo_dir/scripts/install.py" --copy "$@"
printf 'Dittobot is installed. Start a new Codex session if $dittobot does not appear right away.\n'
