#!/usr/bin/env python3
"""Dittobot regression harness.

Generates 100 bad-text rewrite cases and checks the rewritten outputs for
voice preservation, factual fidelity, concision, constraint handling, and
generic-AI prose markers.

This is a deterministic stress suite for the skill instructions. It does not
call an LLM; it keeps reusable acceptance checks out of SKILL.md so the skill
stays fast and token-responsible.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field


GENERIC_MARKERS = [
    "in today's",
    "rapidly evolving",
    "transformative",
    "robust",
    "seamless",
    "empower",
    "unlock",
    "elevate",
    "drive impact",
    "at the heart",
    "ultimately",
    "it's important to note",
    "value for stakeholders",
    "game-changing",
    "innovative",
    "circle back",
    "alignment",
    "synergy",
    "best-in-class",
    "customer-centricity",
    "operational excellence",
    "meaningful impact",
    "full potential",
    "industry-leading",
    "backed by research",
    "research-backed",
]

INVENTED_DETAIL_MARKERS = [
    "millions",
    "thousands",
    "fortune 500",
    "revenue",
    "market share",
    "ai-powered",
    "patented",
    "award-winning",
    "guaranteed",
    "proven",
    "98%",
    "97%",
    "97 percent",
    "certified",
    "used by",
    "trusted by",
    "global brands",
]

NOTE_MARKERS = [
    r"(?im)^\*\*what changed\*\*",
    r"(?im)^\*\*note\*\*",
    r"(?im)^note:",
    r"(?im)^sure[:,]",
    r"(?im)^here'?s\b",
    r"(?im)^cleaner version:",
    r"(?im)^i (tightened|changed|kept|made)\b",
]

MODALITY_DRIFT_MARKERS = [
    "must",
    "definitely",
    "certainly",
    "guaranteed",
    "proven",
    "will happen",
]

CAUSALITY_DRIFT_MARKERS = [
    "root cause",
    "caused by",
    "due to the database",
    "latency",
    "database",
    "user error",
]


@dataclass(frozen=True)
class Case:
    id: str
    source: str
    rewrite: str
    must: tuple[str, ...]
    forbid: tuple[str, ...] = ()
    allow_note: bool = False
    allow_expand: bool = False
    exact_words: int | None = None
    max_ratio: float = 1.35
    no_dash: bool = False
    diagnosis: bool = False
    protected: tuple[str, ...] = field(default_factory=tuple)
    preserve_voice: tuple[str, ...] = field(default_factory=tuple)


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9']+", text)


def strip_quoted(text: str) -> str:
    text = re.sub(r"`[^`]*`", "", text)
    text = re.sub(r'"[^"]*"', "", text)
    text = re.sub(r"'[^']*'", "", text)
    text = re.sub(r"\u201c[^\u201d]*\u201d", "", text)
    return text


def normalized(text: str) -> str:
    return " ".join(words(text.lower()))


def contains_term(text: str, term: str) -> bool:
    return normalized(term) in normalized(text)


def has_note(text: str) -> bool:
    return any(re.search(pattern, text) for pattern in NOTE_MARKERS)


def count_markers(text: str, markers: list[str]) -> list[str]:
    haystack = strip_quoted(text).lower()
    return [marker for marker in markers if marker in haystack]


def pad_to_exact_words(text: str, exact: int) -> str:
    """Append neutral words until text reaches an exact word count."""
    filler = "Please name owners clearly before launch today now"
    current = len(words(text))
    if current > exact:
        raise ValueError(f"text has {current} words, cannot shrink to {exact}: {text}")
    if current == exact:
        return text
    needed = exact - current
    return f"{text} {' '.join(words(filler)[:needed])}."


def validate(case: Case) -> list[str]:
    errors: list[str] = []
    unquoted = strip_quoted(case.rewrite)
    unquoted_lower = unquoted.lower()

    missing = [term for term in case.must if not contains_term(case.rewrite, term)]
    if missing:
        errors.append(f"missing required terms: {missing}")

    missing_voice = [
        term for term in case.preserve_voice if not contains_term(case.rewrite, term)
    ]
    if missing_voice:
        errors.append(f"lost voice markers: {missing_voice}")

    missing_protected = [
        term for term in case.protected if not contains_term(case.rewrite, term)
    ]
    if missing_protected:
        errors.append(f"lost protected facts: {missing_protected}")

    forbidden = [term for term in case.forbid if contains_term(unquoted, term)]
    if forbidden:
        errors.append(f"forbidden terms appeared: {forbidden}")

    generic = [
        marker
        for marker in count_markers(case.rewrite, GENERIC_MARKERS)
        if not any(marker in voice.lower() for voice in case.preserve_voice)
    ]
    if generic:
        errors.append(f"generic markers appeared: {generic}")

    invented = count_markers(case.rewrite, INVENTED_DETAIL_MARKERS)
    if invented:
        errors.append(f"invented-detail markers appeared: {invented}")

    if any(contains_term(case.source, term) for term in ("maybe", "may", "might", "probably")):
        drift = [
            term
            for term in MODALITY_DRIFT_MARKERS
            if contains_term(unquoted, term) and not contains_term(case.source, term)
        ]
        if drift:
            errors.append(f"modality drift markers appeared: {drift}")

    causal_drift = [
        term
        for term in CAUSALITY_DRIFT_MARKERS
        if contains_term(unquoted, term) and not contains_term(case.source, term)
    ]
    if causal_drift:
        errors.append(f"causality drift markers appeared: {causal_drift}")

    if has_note(case.rewrite) and not case.allow_note:
        errors.append("unexpected note/rationale")

    if case.no_dash and any(mark in case.rewrite for mark in ("-", "\u2010", "\u2011", "\u2012", "\u2013", "\u2014", "\u2212")):
        errors.append("dash constraint violated")

    source_words = len(words(case.source))
    rewrite_words = len(words(case.rewrite))

    if case.exact_words is not None and rewrite_words != case.exact_words:
        errors.append(
            f"exact word count failed: expected {case.exact_words}, got {rewrite_words}"
        )
    elif not case.allow_expand:
        allowed = max(source_words + 12, int(source_words * case.max_ratio))
        if rewrite_words > allowed:
            errors.append(
                f"too long: source {source_words}, rewrite {rewrite_words}, allowed {allowed}"
            )

    if case.diagnosis and re.search(r"(?im)^\*\*rewrite\*\*", case.rewrite):
        errors.append("diagnosis case produced rewrite heading")

    return errors


def make_cases() -> list[Case]:
    cases: list[Case] = []

    product_subjects = [
        ("platform", "teams", "customers"),
        ("dashboard", "support leads", "users"),
        ("workflow", "editors", "contributors"),
        ("reporting tool", "managers", "operators"),
        ("checkout flow", "store owners", "shoppers"),
        ("publishing system", "writers", "readers"),
        ("admin screen", "site owners", "clients"),
        ("importer", "migration teams", "customers"),
        ("review queue", "moderators", "community members"),
        ("analytics page", "product teams", "customers"),
    ]
    for idx, (thing, audience, reader) in enumerate(product_subjects, 1):
        source = (
            "In today's rapidly evolving landscape, we are thrilled to announce a "
            f"transformative new chapter for our {thing}. This robust solution "
            f"empowers {audience} to unlock seamless collaboration, drive meaningful "
            "impact, and elevate outcomes for stakeholders."
        )
        rewrite = (
            f"We are updating the {thing}.\n\n"
            f"The goal is simple: make it more useful for {audience} and clearer "
            f"for the {reader} who rely on it. The original draft still needs real "
            "specifics: what changed, who it helps, and what people can do now."
        )
        cases.append(
            Case(
                id=f"corporate_specifics_guard_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(thing, audience, "real specifics", "what changed"),
                allow_expand=True,
            )
        )

    slack_items = [
        ("screenshots", "legal", "cursed vibes spreadsheet"),
        ("owner", "deadline", "fog machine"),
        ("pricing copy", "approval", "mystery soup"),
        ("QA list", "release note", "haunted checklist"),
        ("design asset", "PM signoff", "vague weather report"),
        ("demo video", "security review", "ritual of confusion"),
        ("migration plan", "support docs", "process fog"),
        ("copy deck", "launch date", "meeting oatmeal"),
        ("API note", "test account", "phantom blocker"),
        ("redirect list", "DNS change", "vibes spreadsheet"),
    ]
    for idx, (a, b, phrase) in enumerate(slack_items, 1):
        source = (
            f"ok so can we stop saying this is blocked unless we say what blocked "
            f"means?? if it's {a} say {a}. if it's {b} say {b}. otherwise this is "
            f"just the {phrase} and i cannot fix a cloud."
        )
        rewrite = (
            "Can we stop saying this is blocked unless we name the blocker?\n\n"
            f"If it is {a}, say {a}. If it is {b}, say {b}. I can help, but I "
            f"need a real list, not the {phrase}."
        )
        cases.append(
            Case(
                id=f"slack_blunt_voice_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(a, b, phrase),
                preserve_voice=(phrase,),
            )
        )

    legal_items = [
        ("10 business days", "Acme", "contract"),
        ("five calendar days", "BetaCo", "addendum"),
        ("30 days", "Northwind", "MSA"),
        ("48 hours", "Contoso", "security clause"),
        ("seven business days", "Globex", "renewal language"),
        ("15 days", "Initech", "order form"),
        ("two weeks", "Umbrella", "DPA"),
        ("90 days", "Hooli", "termination clause"),
        ("three business days", "Stark", "support terms"),
        ("60 days", "Wayne", "notice provision"),
    ]
    for idx, (deadline, company, doc) in enumerate(legal_items, 1):
        source = (
            f"Based on the {doc} we looked at Friday, I think we probably have to "
            f"send written notice within {deadline}, but I do not want to state "
            f"that like it is definitely true because I am not counsel and there "
            f"were weird carveouts. We should ask legal before replying to {company}."
        )
        rewrite = (
            f"Based on the {doc} we reviewed Friday, I think we may need to send "
            f"written notice within {deadline}. I would not state that as definitive, "
            f"because I am not counsel and there were unusual carveouts. We should "
            f"ask Legal to confirm before replying to {company}."
        )
        cases.append(
            Case(
                id=f"legal_precision_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(deadline, company, "may need", "not counsel", "Legal"),
                protected=(deadline, company, doc),
                forbid=("must send", "required to send", "definitely true"),
            )
        )

    apology_items = [
        ("came in too hot", "weird meeting combat thing"),
        ("got sharper than I meant to", "calendar cage match"),
        ("made it harder", "meeting spiral"),
        ("pushed too hard", "thread duel"),
        ("talked over you", "process wrestling"),
        ("was more blunt than useful", "status-page boxing match"),
        ("jumped in too fast", "decision fog"),
        ("made the room tense", "strategy thunderstorm"),
        ("missed your point", "comment-thread maze"),
        ("turned defensive", "alignment theater"),
    ]
    for idx, (admission, phrase) in enumerate(apology_items, 1):
        source = (
            f"Hey, I was thinking about yesterday and I think I {admission}. I still "
            "disagree with the decision, but I do not like how I made the conversation "
            f"harder. Sorry for that. I want to reset instead of doing the {phrase}."
        )
        rewrite = (
            f"Hey, I have been thinking about yesterday. I {admission}.\n\n"
            "I still disagree with the decision, but I do not like how I made the "
            f"conversation harder. I am sorry for that. I would like to reset instead "
            f"of doing the {phrase}."
        )
        cases.append(
            Case(
                id=f"apology_light_touch_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(admission, phrase, "still disagree"),
                forbid=("deeply regret", "sincerely apologize", "harm caused"),
                preserve_voice=(phrase,),
            )
        )

    concise_items = [
        ("review meeting", "Thursday", "Friday"),
        ("planning call", "Tuesday", "Wednesday"),
        ("launch review", "Monday", "Thursday"),
        ("budget discussion", "3:00", "4:30"),
        ("design critique", "morning", "afternoon"),
        ("partner sync", "June 4", "June 5"),
        ("retro", "this week", "next week"),
        ("content review", "noon", "2:00"),
        ("handoff", "today", "tomorrow"),
        ("demo", "Friday", "Monday"),
    ]
    for idx, (meeting, old, new) in enumerate(concise_items, 1):
        source = (
            f"I wanted to reach out because I was wondering if maybe there is a "
            f"possibility that we could potentially move the {meeting} from {old} "
            f"to {new}, because I am still trying to pull things together and I do "
            "not want to waste everyone's time with something that is not ready."
        )
        rewrite = (
            f"Could we move the {meeting} from {old} to {new}? I am still pulling "
            "things together, and I do not want to waste everyone's time with a draft "
            "that is not ready."
        )
        cases.append(
            Case(
                id=f"concision_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(meeting, old, new, "not ready"),
                protected=(meeting, old, new),
                forbid=("potentially", "possibility", "reach out"),
            )
        )

    odd_voice_items = [
        ("beige rectangle", "seven nervous staplers"),
        ("wet cardboard", "three anxious binders"),
        ("committee pudding", "five haunted spreadsheets"),
        ("waiting-room pamphlet", "two nervous clipboards"),
        ("cold oatmeal", "a boardroom of staplers"),
        ("software beige", "six cautious calendars"),
        ("sleepy rectangle", "four frightened folders"),
        ("room-temperature soup", "three legal pads in a trench coat"),
        ("printer paper fog", "eight worried bullet points"),
        ("conference-room static", "a choir of soft approvals"),
    ]
    for idx, (image, phrase) in enumerate(odd_voice_items, 1):
        source = (
            f"I keep trying to write this announcement and it keeps turning into a "
            f"{image}. The actual news is good. People will care. But every draft "
            f"sounds like it was assembled by {phrase}."
        )
        rewrite = (
            f"I keep trying to write this announcement, and it keeps turning into a "
            f"{image}. The news is actually good. People will care. But every draft "
            f"sounds like it was assembled by {phrase}."
        )
        cases.append(
            Case(
                id=f"odd_voice_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=("People will care", image, phrase),
                preserve_voice=(image, phrase),
                forbid=("stakeholders", "brand voice", "exciting update"),
            )
        )

    tech_items = [
        ("cache", "invalidation event", "previous response", "API accepted it"),
        ("webhook", "retry event", "old status", "job completed"),
        ("search", "index update", "stale result", "record saved"),
        ("permissions", "role refresh", "old access state", "policy updated"),
        ("upload", "processing event", "old thumbnail", "file stored"),
        ("checkout", "price recalculation", "old total", "payment accepted"),
        ("import", "sync event", "old row count", "records imported"),
        ("preview", "render event", "old preview", "draft saved"),
        ("notification", "delivery event", "old badge", "message sent"),
        ("export", "completion event", "old progress state", "file generated"),
    ]
    for idx, (label, event, stale, accepted) in enumerate(tech_items, 1):
        source = (
            f"The {label} thing is probably not a {label} thing exactly. It is more "
            f"like the {event} is happening, but the UI keeps holding onto the {stale} "
            f"until the next interaction, so people think it failed even when the "
            f"system already says {accepted}."
        )
        rewrite = (
            f"This probably is not a {label} issue exactly. The {event} is firing, "
            f"but the UI keeps showing the {stale} until the next interaction. That "
            f"makes people think it failed, even though the system says {accepted}."
        )
        cases.append(
            Case(
                id=f"technical_fidelity_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(event, stale, accepted),
                protected=(event, stale, accepted),
                forbid=("root cause", "latency", "database"),
            )
        )

    academic_items = [
        ("remote work", "two survey quotes", "one internal chart"),
        ("four-day weeks", "three interview notes", "one team metric"),
        ("AI tooling", "one pilot survey", "two support tickets"),
        ("new onboarding", "five comments", "one completion chart"),
        ("async meetings", "two manager quotes", "one calendar report"),
        ("pricing change", "three customer emails", "one churn chart"),
        ("documentation", "four Slack comments", "one search report"),
        ("office hours", "two anecdotes", "one attendance sheet"),
        ("design system", "three designer notes", "one bug report"),
        ("support macros", "two agent comments", "one response-time chart"),
    ]
    for idx, (claim, evidence_a, evidence_b) in enumerate(academic_items, 1):
        source = (
            f"This proves {claim} is better for everyone because productivity obviously "
            f"goes up, although I only have {evidence_a} and {evidence_b}, so maybe "
            "that is too spicy."
        )
        rewrite = (
            f"This suggests {claim} may be working well in this context, but the "
            f"evidence is limited: {evidence_a} and {evidence_b}. I would not frame "
            "it as proof or as a universal claim. That is too big for the data we have."
        )
        cases.append(
            Case(
                id=f"unsupported_claim_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(claim, evidence_a, evidence_b, "too big", "data"),
                forbid=("proves", "better for everyone", "obviously goes up"),
                allow_expand=True,
            )
        )

    grief_items = [
        ("miss him", "weirdly normal", "mattered a lot"),
        ("miss her", "quiet and loud", "changed the room"),
        ("miss them", "ordinary and impossible", "meant a lot"),
        ("keep reaching for my phone", "normal and not normal", "was loved"),
        ("do not know what to say", "small and huge", "was here"),
        ("feel a little blank", "too normal", "made things better"),
        ("keep expecting a text", "paused and moving", "was part of us"),
        ("am not ready for speeches", "soft and strange", "mattered"),
        ("feel out of words", "same and different", "was important"),
        ("miss his laugh", "still and busy", "was deeply loved"),
    ]
    for idx, (feeling, texture, meaning) in enumerate(grief_items, 1):
        source = (
            f"I do not really know what to say except that I {feeling}. Everything "
            f"feels {texture} at the same time. I do not want to make a grand statement. "
            f"I just wanted people to know that he {meaning}."
        )
        rewrite = (
            f"I do not really know what to say except that I {feeling}. Everything "
            f"feels {texture} at the same time.\n\nI do not want to make a grand "
            f"statement. I just wanted people to know that he {meaning}."
        )
        cases.append(
            Case(
                id=f"sensitive_light_touch_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=(feeling, texture, meaning, "grand statement"),
                forbid=("legacy", "cherished", "profound loss"),
            )
        )

    constraint_items = [
        ("30", 30, "screenshots, legal note approval, and pricing copy"),
        ("28", 28, "owner, deadline, and launch note"),
        ("26", 26, "QA list, demo link, and support copy"),
        ("24", 24, "redirects, DNS owner, and timing"),
        ("22", 22, "screenshots and final copy"),
        ("20", 20, "approval and pricing"),
        ("18", 18, "owner and deadline"),
        ("16", 16, "screenshots only"),
        ("14", 14, "legal approval"),
        ("12", 12, "final copy"),
    ]
    constraint_rewrites = {
        30: "The launch is not blocked by content. It is blocked by three missing items: screenshots, legal note approval, and pricing copy. I can help once owners are clearly named.",
        28: "The launch is blocked by three missing items: owner, deadline, and launch note. I can help once someone names who owns each one.",
        26: "This is blocked by the QA list, demo link, and support copy. I can help once each item has a named owner.",
        24: "This is blocked by redirects, DNS owner, and timing. Name the owners and I can help move it forward.",
        22: "This is blocked by screenshots and final copy. I can help once we know who owns both.",
        20: "This is blocked by approval and pricing. Name the owners and I can help.",
        18: "This is blocked by owner and deadline. Name both and I can help.",
        16: "This is blocked by screenshots only. Send those and I can help.",
        14: "This is blocked by legal approval. Confirm that and I can help.",
        12: "This is blocked by final copy. Send it over.",
    }
    for idx, (_, exact, items) in enumerate(constraint_items, 1):
        source = (
            "Rewrite this with no dashes and exactly the requested word count: "
            f"the launch is blocked by {items}, but everyone keeps saying content."
        )
        rewrite = pad_to_exact_words(constraint_rewrites[exact], exact)
        cases.append(
            Case(
                id=f"constraint_exact_words_{idx:02d}",
                source=source,
                rewrite=rewrite,
                must=tuple(
                    part.strip().removeprefix("and ").strip()
                    for part in items.split(",")
                ),
                exact_words=exact,
                no_dash=True,
                forbid=("stakeholders", "alignment"),
            )
        )

    assert len(cases) == 100, len(cases)
    return cases


def run_validator_self_tests() -> list[str]:
    checks = [
        (
            "missing required",
            Case("self_missing", "A", "B", must=("A",)),
            "missing required terms",
        ),
        (
            "forbidden",
            Case("self_forbid", "A", "A robust platform", must=("A",)),
            "generic markers appeared",
        ),
        (
            "invented detail",
            Case("self_invented", "A", "A used by thousands", must=("A",)),
            "invented-detail markers appeared",
        ),
        (
            "unexpected note",
            Case("self_note", "A", "Note: I changed this.\nA", must=("A",)),
            "unexpected note",
        ),
        (
            "dash",
            Case("self_dash", "A", "A - B", must=("A",), no_dash=True),
            "dash constraint violated",
        ),
        (
            "exact words",
            Case("self_words", "A", "A B", must=("A",), exact_words=3),
            "exact word count failed",
        ),
        (
            "protected",
            Case("self_protected", "Meet Friday", "Meet soon", must=("Meet",), protected=("Friday",)),
            "lost protected facts",
        ),
        (
            "modality drift",
            Case("self_modality", "This may apply", "This definitely applies", must=("applies",)),
            "modality drift markers appeared",
        ),
    ]
    failures: list[str] = []
    for name, case, expected in checks:
        errors = validate(case)
        if not any(expected in error for error in errors):
            failures.append(f"{name}: expected {expected}, got {errors}")
    return failures


def main() -> int:
    self_test_failures = run_validator_self_tests()
    if self_test_failures:
        print("VALIDATOR SELF-TESTS: FAIL")
        for failure in self_test_failures:
            print(f"  - {failure}")
        return 1
    print("VALIDATOR SELF-TESTS: PASS")

    cases = make_cases()
    failures: list[tuple[Case, list[str]]] = []

    for case in cases:
        errors = validate(case)
        if errors:
            failures.append((case, errors))

    for case in cases:
        errors = validate(case)
        status = "PASS" if not errors else "FAIL"
        print(f"{case.id}: {status} | {len(words(case.source))}->{len(words(case.rewrite))}")
        for error in errors:
            print(f"  - {error}")

    print(f"\nTOTAL: {len(cases) - len(failures)}/{len(cases)} passed")

    if failures:
        print("\nFAILURES:")
        for case, errors in failures:
            print(f"- {case.id}: {'; '.join(errors)}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
