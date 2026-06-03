# Youish

Sharper, tighter rewrites for people who want AI to edit well and still sound like them, not like a committee laminated a thesaurus.

[![Validate](https://github.com/RegionallyFamous/youish/actions/workflows/validate.yml/badge.svg)](https://github.com/RegionallyFamous/youish/actions/workflows/validate.yml)
![License: GPL-2.0-or-later](https://img.shields.io/badge/license-GPL--2.0--or--later-blue.svg)
![Runtime dependencies: none](https://img.shields.io/badge/runtime_deps-none-brightgreen.svg)
[![skills.sh](https://skills.sh/b/RegionallyFamous/youish)](https://skills.sh/RegionallyFamous/youish)

![A risograph-style Youish workshop turning messy notes into clean prose](assets/readme-riso-banner.jpg)

Paste messy notes. Get better, tighter rewrites that still sound like you. That should not be controversial. Apparently we needed a tool anyway.

Youish turns rough drafts, notes, and rants into clear writing without saving every stray line just because it has personality. It is not AI trying to borrow a soul. It edits until the point lands and the voice still feels like yours.

## What Youish Is

Youish is a Codex skill that edits from your source instead of inventing a new voice. It finds the point, improves the structure, cuts clutter, protects facts and uncertainty, keeps useful rough edges, and removes bland AI tells.

It is not a ghostwriter. It is an editor with priorities: make the writing better, make it tighter, and keep it yours. Your claims, taste, stance, and rhythm stay in charge; the reader should not have to excavate the point with a tiny shovel.

It also thinks about what the reader needs: the point, the stakes, the limits, and what to do next. Normal use is still simple: paste the mess and get the clean version.

Sharp and concise is not a vibe here:

- It improves the writing before celebrating the voice.
- It keeps your claims, stance, uncertainty, rhythm, distinctive phrases, and reader action.
- It refuses fake facts, fake certainty, extra jokes, padded voice markers, and generic polish that says less.
- The tests try to break those promises before release does.

## The Point

The answer is not "let AI write for you." The answer is "teach the tool taste, then make it respect your voice."

This started because I watched a real critique turn into a dumb rule. People saw verbose, generic, dash-happy AI writing and jumped straight to "nobody should use AI for writing." I get the rage. Bad AI writing is padded, fake-confident, weirdly bloodless, and somehow proud of saying almost nothing.

I agreed with the diagnosis and hated the prescription.

Banning AI because bad AI writing exists treats the worst workflow as the only workflow. That is a very confident way to lose the plot.

If your AI writes badly, the answer is not to throw away the tool. The answer is to teach it taste, then make it earn the voice markers it keeps.

## Watch It Work

### Stream Of Consciousness

Source:

```text
ok the launch note is somehow both too long and allergic to information. what i actually mean is we fixed the importer bug, people can retry failed rows now, and i need it to sound calm, useful, and not like a haunted changelog wearing a meeting lanyard
```

What Youish fixes/protects:

- The facts are "importer bug fixed" and "failed rows can be retried."
- The writing problem is throat-clearing before the facts.
- The best voice marker is "haunted changelog"; "allergic to information" and "wearing a meeting lanyard" are evidence, not required cargo.

Rewrite:

```text
We fixed the importer bug. Failed rows can now be retried. Keep the launch note calm and useful, not a haunted changelog.
```

### Generic AI Paste

Source:

```text
In today's rapidly evolving landscape, our robust platform empowers teams to unlock seamless collaboration and drive meaningful impact. This sentence is wearing a borrowed suit and refusing to say where it works.
```

What Youish notices:

- The buzzword sentence has no usable facts, so inventing specifics would make it worse.
- The user's real voice is the complaint: "wearing a borrowed suit" and "refusing to say where it works."

Rewrite:

```text
This draft is wearing a borrowed suit and refusing to say where it works. Add what changed, who it helps, and what people can do now.
```

### Voice Worth Keeping

Source:

```text
This draft is not bad. It just walks into the room, apologizes for existing, and hands the reader a damp napkin labeled strategy.
```

What Youish fixes/protects:

- The image carries the point, so sanding it down would make the writing worse.
- The rewrite can still tighten the sentence around that image.

Rewrite:

```text
The draft is not bad. It walks in, apologizes for existing, and hands the reader a damp napkin labeled strategy.
```

### Precision-Sensitive Writing

Source:

```text
I think we probably need to send notice within 10 business days, but I am not counsel, the clause had weird carveouts, and I do not want to turn "maybe" into a courtroom kazoo.
```

What Youish fixes/protects:

- "Probably," "I think," and "not counsel" are precision, not clutter.
- The rewrite must keep the strange but useful warning: do not turn "maybe" into a courtroom kazoo.

Rewrite:

```text
I think notice may be due within 10 business days, but I am not counsel and the clause had weird carveouts. I do not want to turn "maybe" into a courtroom kazoo.
```

### Mixed Human Stance

Source:

```text
I am a little angry that people saw bad AI writing and decided the answer was banning the tool, but I am also genuinely excited because we can teach it taste instead of joining the pencils-are-holy club and polishing our typewriters by candlelight.
```

What Youish fixes/protects:

- The anger and hope both matter.
- The best weird marker is "pencils-are-holy club"; the typewriter bit is fun, but not necessary.

Rewrite:

```text
I am annoyed that people saw bad AI writing and decided the answer was banning the tool. I am also genuinely excited, because we can teach it taste instead of joining the pencils-are-holy club.
```

## What Skeptics Are Right About

The AI-writing backlash has receipts. People have seen enough soulless, padded, fake-confident slop to be annoyed. Good. Stay annoyed. Just aim the annoyance at the workflow instead of pretending the tool has only one possible setting.

- **"It sounds like nobody."** Correct, if you ask it to invent a voice. Youish starts from your words. The stance, rhythm, humor, pressure, and weird little phrase are already there.
- **"It gets bloated."** Bad AI writes like it is being paid by the clause. Youish cuts filler and returns the rewrite without a lecture unless you ask for one.
- **"It flattens everyone into the same house style."** Yes, if everyone accepts the first generic draft. Youish keeps dry jokes, justified edge, warmth, awkwardness, and useful rough edges.
- **"It invents confidence."** That is a real failure mode. Youish does not add numbers, customers, citations, examples, legal certainty, or convenient details that were not in the source.
- **"It hides who wrote it."** Editing is not the same as outsourcing authorship. Youish keeps your claims, taste, and decisions in charge.
- **"The tells give it away."** Dashes are not the crime. Predictability is. Youish can obey no-dash rules, but the deeper fix is cadence and taste.

The problem is not using AI. The problem is accepting the first bland answer, then blaming the whole category because nobody steered.

So the behavior is deliberately boring where bad AI gets cute:

- If the draft has no facts, Youish will not invent facts.
- If the draft has uncertainty, Youish keeps the uncertainty.
- If the draft has a weird good phrase, Youish protects it.
- If the draft is bloated, Youish cuts before it decorates.
- If a constraint says no dashes, no notes, or exactly 40 words, Youish treats that like the job.

## When Not To Use It

Youish needs source text or a real voice sample. It is not for making up legal, medical, financial, academic, or factual certainty. It should not bypass publication policies, disclosure rules, or common sense around private data.

When disclosure matters, say the true thing: edited with AI from my draft, grammar and clarity assistance only, or AI-assisted line edit with facts checked by me. Authorship is not a magic spell. Be honest about the workflow and keep responsibility where it belongs.

| Good For | Not For |
|---|---|
| Emails, posts, notes, announcements, bios, captions, messy drafts, and half-formed thoughts | Inventing facts, citations, customers, legal certainty, medical certainty, or financial advice |
| Making a real draft cleaner, sharper, shorter, warmer, stranger, or more readable | Hiding authorship, bypassing disclosure rules, or pretending nobody edited anything |
| Preserving a personal, team, or publication voice | Replacing judgment, policy, review, or the writer's responsibility |

## Use It

Install Youish from inside Codex:

```text
Use $skill-installer to install Youish from GitHub repo RegionallyFamous/youish. Use path "skills/youish" and install it as "youish".
```

Restart Codex, then most prompts can stay this boring:

```text
Use $youish on this:

[paste the messy draft, notes, rant, email, announcement, post, caption, or half-formed thought]
```

To verify the install with a real rewrite:

```text
Use $youish on this and return only the rewrite:

ok the launch note is somehow both too long and allergic to information. what i actually mean is we fixed the importer bug, people can retry failed rows now, and i need it to sound calm, useful, and not like a haunted changelog wearing a meeting lanyard
```

A good result should frontload the facts: `importer bug fixed` and `failed rows can be retried`. It should cut the throat-clearing and keep at least one live voice marker, like `haunted changelog`.

That is the point. Drop in the stream of consciousness; get back the version that sounds like you after sleep, coffee, and one more pass.

You do not need to say "preserve my voice," "do not add facts," or "keep uncertainty." That is the job. Add instructions only when you mean it: exact word count, no dashes, a specific audience, options, diagnosis-only, or show what changed.

More install paths live in [Install](https://github.com/RegionallyFamous/youish/wiki/Install). Skills.sh, release ZIPs, and plugin packaging live in [Distribution](https://github.com/RegionallyFamous/youish/wiki/Distribution).

## Proof, Not Vibes

Youish's quality story is not "trust me, it feels good."

The public scorecard tests the things bad AI writing usually breaks: facts, uncertainty, constraints, concision, output shape, and whether the edit actually improves the draft.

This does not prove literary taste. It proves Youish keeps the constraints it claims to protect. Taste up front, receipts in the back.

The full proof matrix lives in [Validation](https://github.com/RegionallyFamous/youish/wiki/Validation), with release scorecard details in [Live Eval And Scorecards](https://github.com/RegionallyFamous/youish/wiki/Live-Eval-And-Scorecards).

## The Useful Boring Stuff

The manuals live in the wiki so the README can stay focused on the why and the examples:

- [Install](https://github.com/RegionallyFamous/youish/wiki/Install)
- [Validation](https://github.com/RegionallyFamous/youish/wiki/Validation)
- [Youish Lab](https://github.com/RegionallyFamous/youish/wiki/Youish-Lab)
- [Voice Profiles](https://github.com/RegionallyFamous/youish/wiki/Voice-Profiles)
- [Privacy And Fixtures](https://github.com/RegionallyFamous/youish/wiki/Privacy-And-Fixtures)
- [Live Eval And Scorecards](https://github.com/RegionallyFamous/youish/wiki/Live-Eval-And-Scorecards)
- [Distribution](https://github.com/RegionallyFamous/youish/wiki/Distribution)
- [Research Thread](https://github.com/RegionallyFamous/youish/wiki/Research-Thread)
- [Release Checklist](https://github.com/RegionallyFamous/youish/wiki/Release-Checklist)

## About The Name

Youish means the output should still sound like the writer: cleaned up, sharpened, and more readable, but not flattened into generic AI paste.

## License

SPDX-License-Identifier: GPL-2.0-or-later.

Copyright (C) 2026 Regionally Famous.

Youish does not claim ownership of text you write, rewrite, or edit with it. Your drafts and outputs are yours.
