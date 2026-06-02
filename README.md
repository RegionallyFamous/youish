# Dittobot

Paste messy notes, rough drafts, or thought dumps; get a voice-faithful rewrite that sounds like you, not like a committee laminated a thesaurus.

[![Validate](https://github.com/RegionallyFamous/dittobot/actions/workflows/validate.yml/badge.svg)](https://github.com/RegionallyFamous/dittobot/actions/workflows/validate.yml)
![License: GPL-2.0-or-later](https://img.shields.io/badge/license-GPL--2.0--or--later-blue.svg)
![Runtime dependencies: none](https://img.shields.io/badge/runtime_deps-none-brightgreen.svg)

## Quick Start

Dittobot is for the moment when your brain has the idea but the draft is still a pile of sentence laundry.

```bash
git clone https://github.com/RegionallyFamous/dittobot.git
cd dittobot
python3 scripts/install.py
```

Then use it like this:

```text
Use $dittobot on this:

ok the launch note is somehow both too long and says nothing. what i actually mean is we fixed the importer bug, people can retry failed rows now, and i need it to sound calm but not like a haunted changelog
```

Dittobot should preserve your voice, protect your facts, remove the fog, and hand back the finished version by default.

It returns something like:

```text
We fixed the importer bug. People can retry failed rows now, so the launch note should be calm and useful, not a haunted changelog.
```

You do not need to explain the whole job. Paste the mess; Dittobot infers the edit.

## Why This Exists

The answer is not "never use AI." The answer is "teach the tool your voice."

Generic AI writing is real. It can be padded, shiny, over-balanced, weirdly eager, allergic to risk, and full of phrases nobody says unless they are trapped in a webinar. But banning AI because bad AI writing exists is like banning spellcheck because someone once accepted the wrong suggestion. It treats the worst workflow as the only workflow.

If your AI writes badly, the answer is not to throw away the tool. The answer is to teach it taste.

Dittobot is built around that idea. It does not try to replace the writer. It tries to become the editor who knows what the writer sounds like, what they care about, what they would never say, and where their draft is hiding the good part under three blankets of filler.

That matters because AI writing tools can flatten expression. Research on human-AI co-writing has found that writers care about preserving authentic voice and that personalization can help when it supports the writer rather than replacing them. Other work has found AI suggestions can homogenize writing toward dominant styles and reduce cultural nuance. Dittobot is a practical answer to that risk: keep the speed, reject the flattening.

- ["It was 80% me, 20% AI": Seeking Authenticity in Co-Writing with Large Language Models](https://arxiv.org/abs/2411.13032)
- [AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances](https://arxiv.org/abs/2409.11360)

## What Dittobot Does

Dittobot is a Codex skill for rewriting, tightening, diagnosing, and punching up prose while preserving the user's voice.

It:

- turns raw notes, rants, fragments, and thought dumps into usable prose by default;
- preserves voice, intent, facts, stance, rhythm, humor, and formality;
- tightens prose without sanding off the human parts;
- removes bland AI tells like generic openers, shiny abstractions, tidy triples, and dash dependency;
- avoids invented specifics, fake confidence, unsupported claims, and convenient made-up evidence;
- keeps private ledgers for constraints, claims/facts, and voice markers;
- uses fast editorial gates by default and expands into a 20-pass checklist for hard work;
- includes a deterministic 100-case fixture harness plus an optional live model smoke test;
- ships a local rewrite audit tool for checking arbitrary source/rewrite pairs without calling a model;
- ships a rewrite provenance report so users can see what was preserved, lost, or riskily added;
- includes a case lab for turning real bad rewrites into focused regression fixtures;
- supports compact reusable voice profile cards, fact fences, and local voice probes.

Dittobot is not a ghostwriter. It is a voice-preserving editor. The goal is not "sounds professional." The goal is "sounds like you on a very good writing day."

## For Writers Worried About Voice Loss

Dittobot edits from the draft outward. It treats your wording as evidence, not debris.

It preserves odd phrasing when the odd phrasing carries intent. It keeps justified anger, tenderness, awkwardness, bluntness, and dry humor when those are part of the point. It treats smoothness as optional. Sometimes the best edit is one sentence left alone.

## What Dittobot Will Not Do

Dittobot will not:

- invent anecdotes, claims, citations, customers, numbers, or evidence;
- add "humanizing" typos or fake casualness;
- mimic a famous living writer;
- disguise unethical AI use;
- override legal, medical, financial, academic, or technical precision;
- turn every draft into a shiny professional announcement.

## Why Handwriting Everything Is The Wrong Fight

Handwriting every draft to prove you are not using AI is not virtue. It is a slow ritual of avoidance. If the real issue is "the tool does not write like me yet," then refusing to teach it your taste is, frankly, insane.

The real problem is not that AI can help with writing. The real problem is letting an untrained tool flatten your work into beige committee paste, then pretending the only options are "publish the paste" or "never use the tool." That is the wrong fight.

The sane move is to encode taste.

Teach the system what to preserve. Teach it which claims it cannot change. Teach it when to be blunt, when to be warm, when to leave the weird phrase alone because the weird phrase is the whole point. Teach it that a better sentence is not always a smoother sentence. Teach it that "less AI-sounding" does not mean adding typos, fake casualness, or random little messes. It means restoring intent.

Most of the time, teaching it means giving it your actual messy draft, not writing a perfect prompt.

Writing with AI should not mean outsourcing your voice. It should mean giving your voice a better editor.

## About The Name

The name is a playful nod to Ditto from Pokemon: the whole trick is transformation without losing the original shape. Also, "ditto" is a perfectly normal English word, so please do not sue me, Nintendo. Dittobot is unofficial and unaffiliated, just a wink from one weird little tool to another.

## Install

Requirements:

- Codex with skills support;
- Python 3 only for validation scripts;
- a macOS/Linux shell for the symlink commands below. Windows users can use a copy install instead.

Clone the repo:

```bash
git clone https://github.com/RegionallyFamous/dittobot.git
cd dittobot
```

Install it into your Codex skills folder:

```bash
python3 scripts/install.py
```

The installer backs up an existing `~/.codex/skills/dittobot`, creates a symlink by default, and runs the install verifier. Use `--copy` if you cannot or do not want to symlink; copy installs include only the installable skill package files:

```bash
python3 scripts/install.py --copy
```

Manual symlink install:

```bash
mkdir -p ~/.codex/skills
if [ -e ~/.codex/skills/dittobot ]; then
  mv ~/.codex/skills/dittobot ~/.codex/skills/dittobot.backup.$(date +%s)
fi
ln -s "$(pwd)" ~/.codex/skills/dittobot
```

Symlinks are preferred because they prevent drift. If you need a copy, rerun the installer so stale package files are replaced cleanly:

```bash
python3 scripts/install.py --copy
```

Then invoke it as `$dittobot`.

What gets installed: `SKILL.md`, `agents/openai.yaml`, icon assets, optional references, and helper scripts for validation, installation, ad hoc rewrite audits, rewrite provenance reports, regression-case scaffolding, voice probing, live reporting, and optional live eval. Normal Dittobot use does not run or load the scripts or references.

Check that your installed skill still matches the repo:

```bash
python3 scripts/check_install.py
```

Build a local Codex plugin package when you want a plugin-style distribution artifact:

```bash
python3 scripts/build_plugin.py
python3 scripts/check_plugin_package.py dist/dittobot-plugin --version 0.2.0
```

The generated package lives in `dist/dittobot-plugin` and is ignored by git. It contains `.codex-plugin/plugin.json`, Codex UI metadata, original Dittobot icon assets, and the installable skill under `skills/dittobot/`.

## Use

Most of the time, do not over-instruct it. Drop in the mess.

```text
Use $dittobot on this:

[paste the stream of consciousness, rough email, notes, rant, draft, or half-formed announcement]
```

These are defaults, not chores:

- preserve voice, intent, facts, stance, rhythm, humor, and formality;
- tighten the writing and remove bland AI tells;
- keep weird phrasing when the weird phrasing works;
- avoid invented specifics, fake confidence, and unsupported claims;
- preserve uncertainty in legal-ish, technical, academic, medical, financial, or factual text;
- return only the rewrite unless you ask for notes, options, diagnosis, or a comparison.

Only add instructions when you need a hard constraint or a special mode:

```text
Use $dittobot on this in exactly 40 words. No dashes.
```

```text
Use $dittobot to infer a reusable voice profile from these samples. Do not rewrite yet.
```

```text
Use $dittobot to show what changed and why.
```

## Examples

Generic AI:

```text
In today's rapidly evolving landscape, our robust platform empowers teams to unlock seamless collaboration and drive meaningful impact.
```

Dittobot rewrite:

```text
We are updating the platform so teams can find the work, make a decision, and move on. The draft still needs specifics: what changed, who it helps, and what people can do now.
```

Why it works: it cuts the shiny abstractions, keeps the claim modest, and asks for real details instead of inventing them.

Voicey draft:

```text
This draft is not bad. It just walks into the room and immediately apologizes for existing.
```

Dittobot rewrite:

```text
The draft is not bad. It just walks into the room and immediately apologizes for existing. The idea works; the framing is getting in its way.
```

Why it works: it keeps the dry image because that is the writer's fingerprint.

Precision-sensitive draft:

```text
I think we probably need to send notice within 10 business days, but I am not counsel and the clause had weird carveouts.
```

Dittobot rewrite:

```text
I think we may need to send notice within 10 business days. I would not state that as definitive, though, because I am not counsel and the clause had unusual carveouts.
```

Why it works: it improves clarity without turning uncertainty into legal certainty.

## Validate

Run the deterministic fixture validator:

```bash
python3 scripts/validate_skill.py
python3 scripts/regression_100.py
python3 scripts/audit.py --source "I think notice may be due in 10 days." --rewrite "I think notice may be due in 10 days." --preserve-uncertainty --protected "10 days"
python3 scripts/rewrite_report.py --source "I think notice may be due in 10 days." --rewrite "I think notice may be due in 10 days." --protected "10 days" --preserve-uncertainty
python3 scripts/case_lab.py --case-id sample_case_01 --source "rough but redacted source" --rewrite "clean but still redacted rewrite" --must "redacted"
python3 scripts/voice_probe.py --sample "This draft is not bad. It just apologizes for existing."
python3 scripts/build_plugin.py --version 0.2.0 --validator ""
python3 scripts/check_plugin_package.py dist/dittobot-plugin --version 0.2.0
python3 -m py_compile scripts/*.py
tmpdir="$(mktemp -d)"
mkdir -p "$tmpdir/codex-skills"
ln -s "$(pwd)" "$tmpdir/codex-skills/dittobot"
python3 scripts/check_install.py --install-dir "$tmpdir/codex-skills/dittobot"
python3 scripts/install.py --install-dir "$tmpdir/codex-skills/dittobot-installed"
python3 scripts/install.py --install-dir "$tmpdir/codex-skills/dittobot-installed"
python3 scripts/install.py --copy --install-dir "$tmpdir/codex-skills/dittobot-installed-copy"
python3 scripts/check_install.py --install-dir "$tmpdir/codex-skills/dittobot-installed-copy"
```

Expected result:

```text
Skill repo validation passed.
VALIDATOR SELF-TESTS: PASS
TOTAL: 100/100 passed
PASS | source_words=9 rewrite_words=9
# Rewrite Report
# Review before committing: keep fixtures redacted and focused.
# Voice Probe
Plugin package check passed: ...
Installed skill matches repo (symlink): ...
Installed symlink: ...
Installed copy: ...
Installed skill matches repo (copy): ...
```

This validates the 100 primary fixtures, the validator itself, profile-boundary contracts, mutation checks against bad outputs, the ad hoc audit tool, the rewrite provenance report, the case scaffold generator, the plugin package, and the installer. It covers corporate slop, blunt Slack, legal precision, apologies, concision, odd voice, technical notes, unsupported claims, sensitive writing, messy thought dumps, reusable profile boundaries, format preservation, diagnosis-only requests, and exact constraint handling.

## Dittobot Lab

Dittobot is intentionally small in normal use, but the repo ships a little lab bench for people who want to prove the editor is behaving.

Probe local writing samples for observable voice signals without calling a model:

```bash
python3 scripts/voice_probe.py samples/*.local.md
```

Use those signals to build a compact profile card:

```md
## Use
- Plain words, dry contrast, and short useful openings.

## Avoid
- Corporate fog, tidy triples, forced cheer, and "professional" filler.

## Rhythm/Diction
- Mostly short sentences with the occasional sideways image.

## Protected quirks
- Keep the weird little joke when it carries the point.

## Evidence phrases
- "haunted changelog"
- "walks into the room and apologizes for existing"

## When not to apply
- Legal, medical, financial, crisis, or customer-facing precision work.

## Editing rules
- Tighten hard, but do not sand off the speaker.
```

Profiles transfer taste, not old facts. Current draft facts, current audience, and explicit constraints win.

Use fact fences when a draft has material that must survive:

```text
[[keep: Acme, 10 business days, not counsel]]
[[claim: may need to send notice]]
[[voice: haunted changelog]]
[[avoid: Legal has approved, robust, seamless]]
[[boundary: casual Slack voice does not apply to the customer notice]]
```

Audit any source/rewrite pair without calling a model:

```bash
python3 scripts/audit.py \
  --source "[[keep: 10 days]] [[claim: may be due]] I think notice may be due in 10 days." \
  --rewrite "Notice is due in 10 days." \
  --preserve-uncertainty
```

Failed audits include stable failure codes such as `lost_uncertainty`, `generic_ai_marker`, `lost_protected_fact`, and `unexpected_wrapper`, plus broader buckets such as `uncertainty_drift` or `fact_loss`.

Generate a provenance report when you want to show what survived the edit and what got risky:

```bash
python3 scripts/rewrite_report.py \
  --source "[[keep: 10 days]] [[voice: haunted changelog]] I think notice may be due in 10 days." \
  --rewrite "Notice is due in 10 days." \
  --preserve-uncertainty
```

The report is deterministic and model-free. It shows word-count movement, protected-fact status, voice-marker status, added numeric claims, generic AI markers, invented-detail markers, and stable failure codes.

Turn a real, redacted bad rewrite into a fixture skeleton:

```bash
python3 scripts/case_lab.py \
  --case-id thought_dump_example_99 \
  --source "messy but redacted source" \
  --rewrite "desired passing rewrite" \
  --voice "dry little joke" \
  --protected "real date" \
  --forbid "In today's landscape"
```

The workflow is simple: find a failure, audit it, convert it into a case, then teach Dittobot once instead of repeating the same warning forever.

Run the optional live model smoke test when you have an API key. This is not a benchmark or a guarantee of voice fidelity; it is a sampled smoke test against one model/API configuration and the deterministic string/marker validators. By default, `--limit` samples across the suite instead of only taking the first cases, and source-only thought-dump fixtures exercise Dittobot's default inference path. A pass means no obvious fixture failures in that sample.

```bash
export OPENAI_API_KEY="sk-..."
python3 scripts/live_eval.py --limit 10
python3 scripts/live_eval.py --prompt-mode source_only --limit 5
python3 scripts/live_eval.py --list-cases --prompt-mode source_only
python3 scripts/live_eval.py --print-prompts --prompt-mode source_only --limit 2
python3 scripts/live_eval.py --case legal_precision_01 --model "$OPENAI_MODEL"
python3 scripts/live_eval.py --limit 20 --model gpt-5-mini --fail-fast --show-output-on-fail --max-total-tokens 50000 --save-jsonl live-eval-results.local.jsonl
python3 scripts/live_eval.py --limit 5 --save-jsonl replayable.local.jsonl --save-raw-output
python3 scripts/live_eval.py --replay-jsonl replayable.local.jsonl
python3 scripts/live_report.py live-eval-results.local.jsonl --fail-under 0.95
python3 scripts/live_report.py live-eval-results.local.jsonl --json
```

Use `--limit`, `--case`, `--prompt-mode source_only`, `--ensure-source-only`, `--fail-fast`, `--max-failures`, or `--max-total-tokens` to keep cost bounded and target the messy-default path. `--list-cases`, `--print-prompts`, and `--replay-jsonl` do not call the API. If `OPENAI_API_KEY` is not set, the live eval skips cleanly unless `--require-key` is passed. Saved JSONL transcripts are local debugging artifacts and must use `.local.jsonl` so they stay ignored. They store hashes by default; add `--save-raw-source` or `--save-raw-output` only when the text is safe to keep locally. Replays require raw `output` records; API-error records without output are preserved as failures. `live_report.py` summarizes pass rates, usage, failure codes, buckets, and the top failed cases.

Custom API URLs are blocked unless you pass `--allow-custom-api-url`; do that only for endpoints you trust with your bearer token and sample text.

## Privacy

Voice samples are personal. Dittobot does not require storing them in this repo. If you create local voice profiles, ledger files, sample files, or live-eval transcripts, prefer `*.local.md`, `*.local.json`, or `*.local.jsonl` so git ignores them. Do not publish anyone's samples unless every person represented in them is comfortable with publication.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contributor guide, [SECURITY.md](SECURITY.md) for privacy/security reporting, and [RELEASE.md](RELEASE.md) for release validation.

Contributions should make the skill sharper without making it bloated. The skill body is intentionally lean so normal use stays fast and token-responsible.

Use the GitHub issue templates for bad rewrites or proposed regression cases. The best reports include a redacted source, the failed output, protected facts, voice markers, and what should have happened.

Good changes usually do one of three things:

- preserve voice more reliably;
- prevent factual or tonal drift;
- add regression coverage for a real writing failure mode.

When adding regression cases, include:

- source text with the bad pattern;
- expected rewritten behavior;
- protected facts and voice markers;
- forbidden generic phrases or drift markers;
- a short reason the case belongs.

Before opening a PR, run:

```bash
python3 scripts/regression_100.py
```

If a change makes the skill more verbose without making it more reliable, it probably belongs in the test harness, not in `SKILL.md`.

## License

SPDX-License-Identifier: GPL-2.0-or-later.

Copyright (C) 2026 Regionally Famous.

Dittobot does not claim ownership of text you write, rewrite, or edit with it. Your drafts and outputs are yours.
