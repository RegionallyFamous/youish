# Release Checklist

Dittobot releases should be boring, tagged, and validated.

1. Update `CHANGELOG.md`.
2. Run local validation:

```bash
PLUGIN_VERSION=0.2.0
python3 scripts/validate_skill.py
python3 scripts/regression_100.py
python3 scripts/audit.py --source "I think notice may be due in 10 days." --rewrite "I think notice may be due in 10 days." --preserve-uncertainty --protected "10 days"
python3 scripts/rewrite_report.py --source "I think notice may be due in 10 days." --rewrite "I think notice may be due in 10 days." --protected "10 days" --preserve-uncertainty
python3 scripts/audit.py --source "I think notice may be due in 10 days." --rewrite "Notice is due in 10 days." --preserve-uncertainty --protected "10 days" --json || true
python3 scripts/rewrite_report.py --source "I think notice may be due in 10 days." --rewrite "Notice is due in 10 days." --protected "10 days" --preserve-uncertainty || true
python3 scripts/case_lab.py --case-id sample_case_01 --source "rough but redacted source" --rewrite "clean but still redacted rewrite" --must "redacted"
python3 scripts/voice_probe.py --sample "This draft is not bad. It just apologizes for existing."
python3 scripts/build_plugin.py --version "$PLUGIN_VERSION" --validator ""
python3 scripts/check_plugin_package.py dist/dittobot-plugin --version "$PLUGIN_VERSION"
python3 -m py_compile scripts/*.py
tmpdir="$(mktemp -d)"
mkdir -p "$tmpdir/codex-skills"
ln -s "$(pwd)" "$tmpdir/codex-skills/dittobot"
python3 scripts/check_install.py --install-dir "$tmpdir/codex-skills/dittobot"
python3 scripts/install.py --install-dir "$tmpdir/codex-skills/dittobot-installed"
python3 scripts/install.py --copy --install-dir "$tmpdir/codex-skills/dittobot-installed-copy"
python3 scripts/check_install.py --install-dir "$tmpdir/codex-skills/dittobot-installed-copy"
```

3. Run focused live-eval inspection without API calls:

```bash
python3 scripts/live_eval.py --list-cases --prompt-mode source_only
python3 scripts/live_eval.py --print-prompts --prompt-mode source_only --limit 2
```

4. Optionally run live model smoke tests with a bounded limit:

```bash
python3 scripts/live_eval.py --prompt-mode source_only --limit 5
python3 scripts/live_eval.py --limit 10 --save-jsonl live-eval-results.local.jsonl
python3 scripts/live_report.py live-eval-results.local.jsonl
```

For offline replay, save raw output only with public-safe fixture text:

```bash
python3 scripts/live_eval.py --limit 5 --save-jsonl replayable.local.jsonl --save-raw-output
python3 scripts/live_eval.py --replay-jsonl replayable.local.jsonl
```

5. Commit, push, and wait for GitHub Actions to pass.
6. When the local plugin validator is available, run it against the generated package:

```bash
PLUGIN_VERSION=0.2.0
python3 scripts/build_plugin.py --version "$PLUGIN_VERSION" --validator path/to/validate_plugin.py --require-validator
```

7. Tag the validated commit, preferably with a signed tag when available:

```bash
PLUGIN_VERSION=0.2.0
git tag -a "v$PLUGIN_VERSION" -m "Dittobot v$PLUGIN_VERSION"
git push origin "v$PLUGIN_VERSION"
```

8. Create a GitHub release from the tag and summarize the validation results.

`main` may be ahead of the latest tagged release. Use releases when you want a stable install point; use `main` when you want the newest improvements.
