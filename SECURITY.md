# Security And Privacy

Dittobot is a local Codex skill, but writing samples are personal. Treat drafts, voice samples, and live-eval transcripts as sensitive.

## Please Do Not Post

- API keys, access tokens, passwords, cookies, or credentials.
- Customer data, private drafts, legal or medical details, HR material, or internal company facts.
- Live-eval transcripts, local profile cards, ledger files, or voice samples that include private text.

Use redacted examples when opening issues.

## Live Eval

`scripts/live_eval.py` sends selected fixture text to the configured API endpoint only when `OPENAI_API_KEY` is set. It refuses custom API URLs unless `--allow-custom-api-url` is passed, and saved transcripts must end in `.local.jsonl`. Transcript saves are hash-only by default; use `--save-raw-source` or `--save-raw-output` only for public-safe text.

`--replay-jsonl` does not call the API, but it requires raw `output` records for deterministic replay. Raw outputs may contain private source text, so only save replayable transcripts locally.

Keep `*.local.jsonl`, `*.local.md`, and `*.local.json` files local. They are debugging artifacts, not release artifacts.

## Reporting

For public-safe bugs, open an issue. For anything involving leaked secrets, private drafts, unsafe transcript handling, or token exposure, contact the maintainer privately before posting details publicly.

If you accidentally commit sensitive text to a fork or branch, rotate affected credentials and remove the content from public history before linking it in an issue.
