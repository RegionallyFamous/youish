# Release Checklist

Dittobot releases should be boring, tagged, and validated.

1. Update `CHANGELOG.md`.
2. Run local validation:

```bash
python3 scripts/validate_skill.py
python3 scripts/regression_100.py
python3 scripts/audit.py --source "I think notice may be due in 10 days." --rewrite "I think notice may be due in 10 days." --preserve-uncertainty --protected "10 days"
python3 scripts/audit.py --source "I think notice may be due in 10 days." --rewrite "Notice is due in 10 days." --preserve-uncertainty --protected "10 days" --json || true
python3 scripts/case_lab.py --case-id sample_case_01 --source "rough but redacted source" --rewrite "clean but still redacted rewrite" --must "redacted"
python3 scripts/voice_probe.py --sample "This draft is not bad. It just apologizes for existing."
python3 -m py_compile scripts/*.py
python3 scripts/check_install.py
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

5. Commit, push, and wait for GitHub Actions to pass.
6. Tag the validated commit, preferably with a signed tag when available:

```bash
git tag -a v0.1.1 -m "Dittobot v0.1.1"
git push origin v0.1.1
```

7. Create a GitHub release from the tag and summarize the validation results.

`main` may be ahead of the latest tagged release. Use releases when you want a stable install point; use `main` when you want the newest improvements.
