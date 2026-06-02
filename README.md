# Dittobot

Voice-faithful rewrites for people who want AI to sound like them, not like a committee laminated a thesaurus.

## Why This Exists

The answer is not "never use AI." The answer is "teach the tool your voice."

Generic AI writing is real. It can be padded, shiny, over-balanced, weirdly eager, allergic to risk, and full of phrases nobody says unless they are trapped in a webinar. But banning AI because bad AI writing exists is like banning spellcheck because someone once accepted the wrong suggestion. It treats the worst workflow as the only workflow.

If your AI writes badly, the answer is not to throw away the tool. The answer is to teach it taste.

Dittobot is built around that idea. It does not try to replace the writer. It tries to become the editor who knows what the writer sounds like, what they care about, what they would never say, and where their draft is hiding the good part under three blankets of filler.

## What Dittobot Does

Dittobot is a Codex skill for rewriting, tightening, diagnosing, and punching up prose while preserving the user's voice.

It:

- preserves voice, intent, facts, stance, rhythm, humor, and formality;
- tightens prose without sanding off the human parts;
- removes bland AI tells like generic openers, shiny abstractions, tidy triples, and dash dependency;
- avoids invented specifics, fake confidence, unsupported claims, and convenient made-up evidence;
- keeps private ledgers for constraints, claims/facts, and voice markers;
- runs a silent 20-pass editorial loop before returning the final rewrite;
- includes a 100-case regression harness so the skill is tested against actual failure modes, not vibes.

Dittobot is not a ghostwriter. It is a voice-preserving editor. The goal is not "sounds professional." The goal is "sounds like you on a very good writing day."

## Why Handwriting Everything Is The Wrong Fight

Handwriting every draft to prove you are not using AI is not virtue. It is a slow ritual of avoidance. If the real issue is "the tool does not write like me yet," then refusing to teach it your taste is, frankly, insane.

The real problem is not that AI can help with writing. The real problem is letting an untrained tool flatten your work into beige committee paste, then pretending the only options are "publish the paste" or "never use the tool." That is the wrong fight.

The sane move is to encode taste.

Teach the system what to preserve. Teach it which claims it cannot change. Teach it when to be blunt, when to be warm, when to leave the weird phrase alone because the weird phrase is the whole point. Teach it that a better sentence is not always a smoother sentence. Teach it that "less AI-sounding" does not mean adding typos, fake casualness, or random little messes. It means restoring intent.

Writing with AI should not mean outsourcing your voice. It should mean giving your voice a better editor.

## Install

Clone the repo:

```bash
git clone https://github.com/RegionallyFamous/dittobot.git
```

Copy or symlink it into your Codex skills folder:

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/dittobot" ~/.codex/skills/dittobot
```

If you prefer a copy:

```bash
cp -R dittobot ~/.codex/skills/dittobot
```

Then invoke it as `$dittobot`.

## Use

```text
Use $dittobot to tighten this email but keep my voice.
```

```text
Use $dittobot to make this less AI-sounding. Do not add facts, do not make it more formal, and keep the dry little joke.
```

```text
Use $dittobot to punch this up, but preserve the weird phrasing where it works.
```

```text
Use $dittobot to clean this legal-ish note without changing the claims or making it sound more certain.
```

```text
Use $dittobot to rewrite this in exactly 40 words. No dashes. No notes.
```

## Validate

Run the regression harness:

```bash
python3 scripts/regression_100.py
```

Expected result:

```text
TOTAL: 100/100 passed
```

The harness covers corporate slop, blunt Slack, legal precision, apologies, concision, odd voice, technical notes, unsupported claims, sensitive writing, and exact constraint handling.

## Contributing

Contributions should make the skill sharper without making it bloated. The skill body is intentionally lean so normal use stays fast and token-responsible.

Good changes usually do one of three things:

- preserve voice more reliably;
- prevent factual or tonal drift;
- add regression coverage for a real writing failure mode.

Before opening a PR, run:

```bash
python3 scripts/regression_100.py
```

If a change makes the skill more verbose without making it more reliable, it probably belongs in the test harness, not in `SKILL.md`.

## License

GPL-2.0-or-later.
