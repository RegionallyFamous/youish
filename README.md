# Dittobot

Voice-faithful rewrites for people who want AI to sound like them, not like a committee laminated a thesaurus.

[![Validate](https://github.com/RegionallyFamous/dittobot/actions/workflows/validate.yml/badge.svg)](https://github.com/RegionallyFamous/dittobot/actions/workflows/validate.yml)
![License: GPL-2.0-or-later](https://img.shields.io/badge/license-GPL--2.0--or--later-blue.svg)
![Runtime dependencies: none](https://img.shields.io/badge/runtime_deps-none-brightgreen.svg)

Paste messy notes, rough drafts, or a stream of consciousness. Dittobot turns the pile into finished prose while preserving the writer underneath it. That should not be controversial, but apparently here we are.

## The Point

The answer is not "never use AI." The answer is "teach the tool your voice."

Generic AI writing is real. It can be padded, shiny, over-balanced, weirdly eager, allergic to risk, and full of phrases nobody says unless they are trapped in a webinar. I get why people hate it. I hate it too. But banning AI because bad AI writing exists is like banning spellcheck because someone accepted the wrong suggestion. It treats the worst workflow as the only workflow, which is a very confident way to lose the plot.

If your AI writes badly, the answer is not to throw away the tool. The answer is to teach it taste.

Dittobot is built around that idea. It is not a ghostwriter. It is a voice-preserving editor. It reads the draft as evidence: what the writer cares about, what they would never say, which facts are sacred, where the joke is hiding, and which strange little phrase is actually the soul of the thing.

That matters because the real risk is not that AI helps people write. The real risk is letting an untrained tool flatten every person into the same beige announcement voice, then pretending the only choices are "publish the paste" or "never touch the tool." That is not ethics. That is a workflow panic attack wearing a name badge.

The better move, the more hopeful move, and frankly the less exhausting move is to encode taste.

## The AI Hater Case, Answered

If you hate AI writing, you are not imagining the problem. A lot of AI writing is bad. Some of it is so bad it feels like a quarterly business review got trapped in a fog machine. The mistake is treating bad defaults as destiny.

**"AI writing has no soul."**

Correct, if the tool is asked to invent a soul from nothing. That is not writing; that is soup with a login screen. Dittobot starts with the writer's actual words. The soul is already there: stance, rhythm, irritation, warmth, uncertainty, humor, pressure, taste. The job is not to manufacture humanity. The job is to stop smothering it.

**"It is too verbose."**

Bad AI loves to explain the obvious, stack soft claims, and keep talking after the point is made. It writes like it is being paid by the clause. Dittobot's default posture is editorial restraint: cut filler, collapse repetition, keep the useful texture, and return the rewrite without a lecture unless the user asks for one.

**"It sounds like slop."**

Slop is not the presence of AI. Slop is unedited output, unsupported claims, fake enthusiasm, generic phrases, and a missing speaker. It is hitting "make better" and accepting "In today's fast-paced world" like that sentence has not already committed enough crimes. Dittobot treats those patterns as failures, with anti-generic checks, protected-fact ledgers, and regression cases for the stuff that makes prose feel machine-polished in the worst way.

**"It all sounds the same."**

Yes, if everyone accepts the first generic draft. That is the whole problem. Dittobot is built to do the opposite: preserve odd phrasing when it works, protect dry jokes, keep justified edge, respect formality when the context needs it, and refuse to turn every draft into the same cheerful memo from the Department of Smooth Nothing.

**"It makes things up."**

That is a real failure mode, so Dittobot is fenced against it. It does not add anecdotes, numbers, customers, citations, examples, legal certainty, or convenient specifics that were not in the source. If the draft needs a fact, the right answer is to leave a modest gap or ask, not invent a tiny documentary in the margins.

**"It hides who really wrote it."**

Using an editor is not the same as outsourcing authorship. The ethical line is control, intent, and disclosure where disclosure matters. Dittobot is designed to keep the user's claims, taste, and decisions in charge. It helps the writer sound more like themselves, not less, which seems like the part everyone should be excited about instead of pretending pencils are morally superior now.

**"People will get lazy."**

Some will. That is true of every tool. But a good AI writing workflow can also make people more deliberate because it forces them to name what should be preserved: facts, stance, audience, boundaries, and voice. The lazy move is not using AI. The lazy move is accepting output without taste, then blaming the entire category because nobody bothered to steer.

**"The dashes give it away."**

Dashes are not the crime. Predictability is. Dittobot can obey a no-dash constraint, but the deeper fix is cadence: shorter sentences where they help, longer ones where they earn the space, and punctuation that sounds like the writer instead of a house style guide with anxiety. We can fix the dashes. We can also fix the thinking underneath them.

## Watch It Work

### Stream Of Consciousness

Source:

```text
ok the launch note is somehow both too long and says nothing. what i actually mean is we fixed the importer bug, people can retry failed rows now, and i need it to sound calm but not like a haunted changelog
```

Dittobot notices:

- The facts are "importer bug fixed" and "failed rows can be retried."
- The voice has a dry little image: "haunted changelog."
- The target is probably a calm launch note, not a motivational announcement.

Rewrite:

```text
We fixed the importer bug. People can retry failed rows now, so the launch note should be calm and useful, not a haunted changelog.
```

### Generic AI Paste

Source:

```text
In today's rapidly evolving landscape, our robust platform empowers teams to unlock seamless collaboration and drive meaningful impact.
```

Dittobot notices:

- The sentence has almost no checkable content.
- The confident tone is not earned.
- Inventing specifics would make it worse.

Rewrite:

```text
We are updating the platform so teams can find the work, make a decision, and move on. The draft still needs specifics: what changed, who it helps, and what people can do now.
```

### Voice Worth Keeping

Source:

```text
This draft is not bad. It just walks into the room and immediately apologizes for existing.
```

Dittobot notices:

- The image is the point.
- A smoother rewrite would be worse.
- The edit should clarify the diagnosis without sanding off the joke.

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

- "Probably," "I think," and "not counsel" are not clutter here. They are precision.
- "10 business days" is protected.
- The rewrite must not turn uncertainty into legal certainty.

Rewrite:

```text
I think we may need to send notice within 10 business days. I would not state that as definitive, though, because I am not counsel and the clause had unusual carveouts.
```

## What Dittobot Is

Dittobot is a Codex skill for rewriting, tightening, diagnosing, and punching up prose while preserving the user's voice, intent, facts, stance, rhythm, humor, and formality.

It runs a quiet editorial loop: protect meaning, identify the voice, tighten the draft, remove bland AI tells, check constraints, and keep iterating when the work is hard. For high-stakes or craft-heavy text, it expands into a silent 20-pass rewrite process.

It ships with a 100-case regression harness, model-free rewrite audits, privacy-first failure-fixture tools, compact voice profile contracts, fact fences, and public release scorecards. The normal user experience is still simple: paste the mess and get the clean version.

## Use It

```bash
git clone https://github.com/RegionallyFamous/dittobot.git
cd dittobot
python3 scripts/install.py
```

Then:

```text
Use $dittobot on this:

[paste the messy draft, notes, rant, email, announcement, post, caption, or half-formed thought]
```

Most of the time, that is enough. Add instructions only for hard constraints like exact word count, no dashes, a specific audience, multiple options, diagnosis-only mode, or a request to show what changed.

## Proof, Not Vibes

Dittobot's quality story is not "trust me, it feels good." The repo includes deterministic checks for voice preservation, protected facts, uncertainty, claim fidelity, source-only thought-dump inference, exact word counts, no-dash constraints, and anti-generic behavior.

The scorecard is intentionally boring: complete-suite gates, stable failure codes, hashes, package checks, and public-safe reporting. The public face can be fired up because the release machinery is disciplined. That is the dream: taste up front, receipts in the back.

## The Useful Boring Stuff

The manuals live in the wiki so the README can stay focused on the why and the examples:

- [Install](https://github.com/RegionallyFamous/dittobot/wiki/Install)
- [Validation](https://github.com/RegionallyFamous/dittobot/wiki/Validation)
- [Dittobot Lab](https://github.com/RegionallyFamous/dittobot/wiki/Dittobot-Lab)
- [Voice Profiles](https://github.com/RegionallyFamous/dittobot/wiki/Voice-Profiles)
- [Privacy And Fixtures](https://github.com/RegionallyFamous/dittobot/wiki/Privacy-And-Fixtures)
- [Live Eval And Scorecards](https://github.com/RegionallyFamous/dittobot/wiki/Live-Eval-And-Scorecards)
- [Release Checklist](https://github.com/RegionallyFamous/dittobot/wiki/Release-Checklist)

## Research Thread

The critique is worth taking seriously. Research on human-AI co-writing has found that writers care about preserving authentic voice and that personalization can help when it supports the writer rather than replacing them. Other work has found AI suggestions can homogenize writing toward dominant styles and reduce cultural nuance. Dittobot is a practical answer to that risk: keep the speed, reject the flattening.

- ["It was 80% me, 20% AI": Seeking Authenticity in Co-Writing with Large Language Models](https://arxiv.org/abs/2411.13032)
- [AI Suggestions Homogenize Writing Toward Western Styles and Diminish Cultural Nuances](https://arxiv.org/abs/2409.11360)

## About The Name

The name is a playful nod to Ditto from Pokemon: the trick is transformation without losing the original shape. Also, "ditto" is a perfectly normal English word, so please do not sue me, Nintendo. Dittobot is unofficial and unaffiliated, just a wink from one weird little tool to another.

## License

SPDX-License-Identifier: GPL-2.0-or-later.

Copyright (C) 2026 Regionally Famous.

Dittobot does not claim ownership of text you write, rewrite, or edit with it. Your drafts and outputs are yours.
