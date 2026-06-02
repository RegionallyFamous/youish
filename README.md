# Dittobot

Voice-faithful rewrites for people who want AI to sound like them, not like a committee laminated a thesaurus.

[![Validate](https://github.com/RegionallyFamous/dittobot/actions/workflows/validate.yml/badge.svg)](https://github.com/RegionallyFamous/dittobot/actions/workflows/validate.yml)
![License: GPL-2.0-or-later](https://img.shields.io/badge/license-GPL--2.0--or--later-blue.svg)
![Runtime dependencies: none](https://img.shields.io/badge/runtime_deps-none-brightgreen.svg)

![A risograph-style Dittobot workshop turning messy notes into clean prose](assets/readme-riso-banner.jpg)

Paste messy notes. Get sharp prose that still sounds like you. That should not be controversial. Apparently we needed a tool anyway.

## Start Here

In Codex, paste this:

```text
Use $skill-installer to install Dittobot from GitHub repo RegionallyFamous/dittobot. Use path "." and install it as "dittobot".
```

Then start a new Codex session and paste the mess:

```text
Use $dittobot on this:

[paste the draft, notes, rant, email, announcement, post, caption, or half-formed thought]
```

That is the streamlined path: let Codex install the skill, then use the skill. No git ceremony. No tiny terminal archaeology expedition before you can fix a sentence.

## What Dittobot Is

Dittobot is a Codex skill that edits from your source instead of inventing a new voice. It finds the point, protects facts and uncertainty, keeps useful rough edges, and cuts bland AI tells.

It is not a ghostwriter. It is a voice-preserving editor: your claims, your taste, your stance, your rhythm, just cleaned up enough that the reader does not have to excavate the point with a tiny shovel.

It also checks the reader's job. The clean version should make the point, stakes, limits, and next action clear after one pass.

For hard work, it expands into a silent 20-pass editorial loop. For proof, the repo ships a 100-case regression suite, model-free rewrite audits, privacy-first failure fixtures, compact voice profiles, fact fences, and public release scorecards.

Normal use is still simple: paste the mess and get the clean version.

Voice-faithful means something testable here:

- It preserves claims, stance, uncertainty, rhythm, distinctive phrases, and reader action.
- It refuses unsupported facts, invented brands, fake certainty, extra jokes, and generic polish that says less.
- It proves those promises with deterministic fixtures, mutation checks, package validation, and release scorecards.

## The Point

The answer is not "let AI write for you." The answer is "teach the tool your voice."

This started because I watched a real critique turn into a dumb rule. People saw verbose, generic, dash-happy AI writing and jumped straight to "nobody should use AI for writing." I get the rage. Bad AI writing is padded, fake-confident, weirdly bloodless, and somehow proud of saying almost nothing.

I agreed with the diagnosis and hated the prescription.

Banning AI because bad AI writing exists treats the worst workflow as the only workflow. That is a very confident way to lose the plot.

If your AI writes badly, the answer is not to throw away the tool. The answer is to teach it taste.

## Watch It Work

### Stream Of Consciousness

Source:

```text
ok the launch note is somehow both too long and says nothing. what i actually mean is we fixed the importer bug, people can retry failed rows now, and i need it to sound calm but not like a haunted changelog
```

Dittobot notices:

- The facts are "importer bug fixed" and "failed rows can be retried."
- The voice marker worth keeping is "haunted changelog."

Rewrite:

```text
We fixed the importer bug. Failed rows can now be retried, so the note can stay calm and useful instead of turning into a haunted changelog.
```

### Generic AI Paste

Source:

```text
In today's rapidly evolving landscape, our robust platform empowers teams to unlock seamless collaboration and drive meaningful impact.
```

Dittobot notices:

- The sentence sounds confident but says almost nothing.
- Inventing specifics would make it worse.

Rewrite:

```text
This draft sounds confident but does not say enough to rewrite safely. Add what changed, who it helps, and what people can do now.
```

### Voice Worth Keeping

Source:

```text
This draft is not bad. It just walks into the room and immediately apologizes for existing.
```

Dittobot notices:

- The image is the point.
- A smoother rewrite would be worse.

Rewrite:

```text
The draft is not bad. It just walks into the room and immediately apologizes for existing. The idea works; the framing is getting in its way.
```

### Precision-Sensitive Writing

Source:

```text
I think we probably need to send notice within 10 business days, but I am not counsel and the clause had weird carveouts.
```

Dittobot notices:

- "Probably," "I think," and "not counsel" are precision, not clutter.
- The rewrite must not turn uncertainty into legal certainty.

Rewrite:

```text
I think we may need to send notice within 10 business days. I would not state that as definitive, though, because I am not counsel and the clause had unusual carveouts.
```

### Mixed Human Stance

Source:

```text
I am a little angry that people saw bad AI writing and decided the answer was banning the tool, but I am also genuinely excited because we can teach it taste instead of pretending pencils are holy now.
```

Dittobot notices:

- The anger and hope both matter.
- The rewrite should be sharp without turning into a personal attack.

Rewrite:

```text
I am annoyed that people saw bad AI writing and decided the answer was banning the tool. But I am also genuinely excited, because we can teach it taste instead of pretending pencils are holy now.
```

## What Skeptics Are Right About

The AI-writing backlash has receipts. People have seen enough soulless, padded, fake-confident slop to be annoyed. Good. Stay annoyed. Just aim the annoyance at the workflow instead of pretending the tool has only one possible setting.

- **"It sounds like nobody."** Correct, if you ask it to invent a voice. Dittobot starts from your words. The stance, rhythm, humor, pressure, and weird little phrase are already there.
- **"It gets bloated."** Bad AI writes like it is being paid by the clause. Dittobot cuts filler and returns the rewrite without a lecture unless you ask for one.
- **"It flattens everyone into the same house style."** Yes, if everyone accepts the first generic draft. Dittobot keeps dry jokes, justified edge, warmth, awkwardness, and useful rough edges.
- **"It invents confidence."** That is a real failure mode. Dittobot does not add numbers, customers, citations, examples, legal certainty, or convenient details that were not in the source.
- **"It hides who wrote it."** Editing is not the same as outsourcing authorship. Dittobot keeps your claims, taste, and decisions in charge.
- **"The tells give it away."** Dashes are not the crime. Predictability is. Dittobot can obey no-dash rules, but the deeper fix is cadence and taste.

The problem is not using AI. The problem is accepting the first bland answer, then blaming the whole category because nobody steered.

## When Not To Use It

Dittobot needs source text or a real voice sample. It is not for making up legal, medical, financial, academic, or factual certainty. It should not bypass publication policies, disclosure rules, or common sense around private data.

When disclosure matters, say the true thing: edited with AI from my draft, grammar and clarity assistance only, or AI-assisted line edit with facts checked by me. Authorship is not a magic spell. Be honest about the workflow and keep responsibility where it belongs.

## Use It

After install, most prompts should be this boring:

```text
Use $dittobot on this:

[paste the messy draft, notes, rant, email, announcement, post, caption, or half-formed thought]
```

That is the point. Drop in the stream of consciousness; get back the version that sounds like you after sleep, coffee, and one more pass.

Pinned GitHub CLI install:

```bash
gh skill install RegionallyFamous/dittobot skills/dittobot --agent codex --scope user --pin v0.2.4
```

Terminal fallback:

```bash
curl -fsSL https://raw.githubusercontent.com/RegionallyFamous/dittobot/v0.2.4/install.sh | DITTOBOT_REF=v0.2.4 bash
```

Codex plugin marketplace source:

```bash
codex plugin marketplace add RegionallyFamous/dittobot --ref v0.2.4
codex plugin add dittobot@dittobot
```

Requires `curl`, `tar`, and Python 3 for the terminal fallback. It installs a copy, backs up an existing Dittobot install, verifies itself, and does not use `sudo`.

Uploadable assets live in [Releases](https://github.com/RegionallyFamous/dittobot/releases): skill ZIP, plugin ZIP, public scorecard, and checksums.

Most of the time, the default prompt is enough. Add instructions only for hard constraints like exact word count, no dashes, a specific audience, options, diagnosis-only mode, or a request to show what changed.

## Proof, Not Vibes

Dittobot's quality story is not "trust me, it feels good." The repo checks voice preservation, protected facts, uncertainty, claim fidelity, exact word counts, no-dash constraints, and anti-generic behavior.

This does not prove literary taste. It proves Dittobot keeps the constraints it claims to protect: facts, uncertainty, length, format, and anti-generic behavior.

| Promise | How It Is Tested |
|---|---|
| Keep the user's voice | Voice marker fixtures, profile contracts, and mutation tests that remove keeper phrases |
| Preserve facts and claims | Protected fact checks, required claims, forbidden assertions, numeric drift checks |
| Preserve uncertainty | Legal and technical cases that fail if "maybe" becomes false certainty |
| Refuse invented details | Unsupported detail markers, invented numbers, and unsupported entity detection |
| Avoid generic AI polish | Buzzword checks plus pattern tests for shiny but empty phrasing |
| Respect constraints | Exact word count, no-dash, format, wrapper, and paragraph-shape checks |
| Turn notes into usable text | Source-only thought-dump cases with artifact cleanup and reader-action checks |

The scorecard is intentionally boring: complete-suite gates, stable failure codes, hashes, package checks, marketplace checks, and public-safe reporting.

Taste up front. Receipts in the back.

## The Useful Boring Stuff

The manuals live in the wiki so the README can stay focused on the why and the examples:

- [Install](https://github.com/RegionallyFamous/dittobot/wiki/Install)
- [Validation](https://github.com/RegionallyFamous/dittobot/wiki/Validation)
- [Dittobot Lab](https://github.com/RegionallyFamous/dittobot/wiki/Dittobot-Lab)
- [Voice Profiles](https://github.com/RegionallyFamous/dittobot/wiki/Voice-Profiles)
- [Privacy And Fixtures](https://github.com/RegionallyFamous/dittobot/wiki/Privacy-And-Fixtures)
- [Live Eval And Scorecards](https://github.com/RegionallyFamous/dittobot/wiki/Live-Eval-And-Scorecards)
- [Distribution](https://github.com/RegionallyFamous/dittobot/wiki/Distribution)
- [Release Checklist](https://github.com/RegionallyFamous/dittobot/wiki/Release-Checklist)

## Research Thread

The critique is worth taking seriously. Research on human-AI co-writing has found that writers care about preserving authentic voice, and other work has found AI suggestions can flatten writing toward dominant styles. Dittobot is a practical answer to that risk: keep the speed, reject the flattening.

- ["It was 80% me, 20% AI": Seeking Authenticity in Co-Writing with Large Language Models](https://arxiv.org/abs/2411.13032): authenticity depends on writers feeling the final piece still carries their choices.
- [AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances](https://arxiv.org/abs/2409.11360): suggestion systems can flatten voice, so voice preservation has to be a first-class requirement.
- [Digital.gov: Principles of plain language](https://digital.gov/guides/plain-language/principles): write for the audience, make the useful action clear, and cut clutter.
- [CPSC: Plain Language Principles](https://www.cpsc.gov/About-CPSC/Policies-Statements-and-Directives/plain-language-principles): plain writing is not dumbed-down writing. It is respect for the reader's time.

## About The Name

The name nods to Ditto from Pokemon: transformation without losing the original shape. Also, "ditto" is a perfectly normal English word, so please do not sue me, Nintendo. Dittobot is unofficial and unaffiliated.

## License

SPDX-License-Identifier: GPL-2.0-or-later.

Copyright (C) 2026 Regionally Famous.

Dittobot does not claim ownership of text you write, rewrite, or edit with it. Your drafts and outputs are yours.
