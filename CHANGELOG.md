# Changelog

## Unreleased

Nothing yet.

## 0.2.2 - 2026-06-02

- Let installed-copy validation tolerate GitHub CLI source-tracking metadata while keeping source repo frontmatter strict.

## 0.2.1 - 2026-06-02

- Add repo plugin marketplace metadata so Dittobot can be exposed as a Codex marketplace source.
- Add one-command release asset building, exact release asset verification, scorecard checksums, and stricter plugin package validation.
- Tighten README examples and skeptic-facing copy so the argument lands faster with less manifesto echo.
- Add optional archive checksum verification to the terminal installer and make the default install ref release-pinned.

## 0.2.0 - 2026-06-02

### Install And Distribution

- Add `$skill-installer`-first setup docs, a no-git terminal installer, and a GitHub CLI-compatible `skills/dittobot` package mirror.
- Make copied installs safer by detecting drift, replacing stale package files cleanly, backing up existing installs, and refusing unsafe targets.
- Add deterministic Codex plugin package building, plugin verification, uploadable skill ZIPs, plugin ZIPs, checksums, and CI release-asset checks.
- Add Codex UI icon assets, wire them into skill/plugin metadata, and add a risograph README banner for the voice-preserving editing metaphor.

### Voice Behavior

- Strengthen voice preservation, emotional anti-flattening, mixed anger/hope handling, format preservation, and source-only thought-dump defaults.
- Add guidance for reader comprehension, user corrections, dialect/code-switching/regional idiom, interpersonal precision, and no-wrapper rewrite output.
- Add reusable fact-fence and voice-profile-card references, real `[[boundary: ...]]` ledger parsing, and compact voice profile contracts.

### Validation And Tooling

- Add portable repo validation, progressive-disclosure word-budget checks, public README copy checks, and GitHub Actions validation.
- Expand deterministic regression coverage for protected facts, claim fidelity, uncertainty, modality drift, causality drift, invented details, no-dash constraints, wrapper detection, ordered terms, artifact cleanup, and exact formatting.
- Add model-free audit, rewrite report, voice probe, case lab, redaction, failure fixture, live report, and scorecard tools.
- Add optional live-model smoke testing with safer API handling, source-only prompt inspection, replayable transcripts, fail-fast controls, hash-only saved transcript defaults, and API-error transcript records.

### Docs And Governance

- Refocus the README on the anti-slop argument, Dittobot's origin story, and in-process examples.
- Move operational runbooks into the GitHub wiki.
- Add bad-rewrite and regression-case issue templates, a pull request checklist, contributor guide, security/privacy guidance, and release checklist.

## 0.1.0

- Initial public Dittobot skill release.
