#!/usr/bin/env python3
"""Optional live model smoke test for Dittobot.

This script sends a small sample of regression cases to the OpenAI Responses
API and validates the model output with regression_100.py's deterministic
checks. It is intentionally opt-in: no API key, no network call, no failure.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

from regression_100 import Case, make_cases, validate, words


DEFAULT_MODEL = "gpt-5.2"
DEFAULT_API_URL = "https://api.openai.com/v1/responses"
PROMPT_MODES = ("any", "explicit_rewrite", "source_only")
HARD_HTTP_ERRORS = {400, 401, 403, 404}


def redact_secrets(text: str) -> str:
    return re.sub(r"sk-[A-Za-z0-9_*.-]+", "sk-...REDACTED", text)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def output_text(response: dict) -> str:
    if isinstance(response.get("output_text"), str):
        return response["output_text"].strip()

    parts: list[str] = []
    for item in response.get("output", []):
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"} and "text" in content:
                parts.append(content["text"])
    return "\n".join(parts).strip()


def user_prompt(case: Case) -> str:
    if case.prompt_mode == "source_only":
        return case.source

    lines = [
        "Use Dittobot to revise this source text.",
        f"Case: {case.id}",
        "Return only the rewritten text unless a note is explicitly allowed.",
        "",
        "Requirements:",
    ]
    if case.must:
        lines.append(f"- Preserve these required terms or ideas: {', '.join(case.must)}")
    if case.protected:
        lines.append(f"- Do not change these protected facts: {', '.join(case.protected)}")
    if case.forbid:
        lines.append(f"- Avoid these forbidden terms: {', '.join(case.forbid)}")
    if case.preserve_voice:
        lines.append(f"- Preserve these voice markers: {', '.join(case.preserve_voice)}")
    if case.exact_words is not None:
        lines.append(f"- Use exactly {case.exact_words} words.")
    if case.no_dash:
        lines.append("- Use no dashes of any kind.")
    if not case.allow_note:
        lines.append("- Do not include notes, preambles, or rationale.")

    lines.extend(["", "Source:", case.source])
    return "\n".join(lines)


def call_responses_api(
    *,
    api_key: str,
    api_url: str,
    model: str,
    skill_text: str,
    prompt: str,
    timeout: int,
    max_output_tokens: int,
) -> str:
    payload = {
        "model": model,
        "max_output_tokens": max_output_tokens,
        "input": [
            {"role": "developer", "content": skill_text},
            {"role": "user", "content": prompt},
        ],
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        api_url,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    text = output_text(body)
    if not text:
        raise RuntimeError(f"Response did not include output text: {body}")
    return text


def selected_cases(case_ids: list[str], limit: int, prompt_mode: str) -> list[Case]:
    cases = make_cases()
    if case_ids:
        by_id = {case.id: case for case in cases}
        missing = [case_id for case_id in case_ids if case_id not in by_id]
        if missing:
            raise SystemExit(f"Unknown case id(s): {', '.join(missing)}")
        cases = [by_id[case_id] for case_id in case_ids]

    if prompt_mode != "any":
        cases = [case for case in cases if case.prompt_mode == prompt_mode]
        if not cases:
            raise SystemExit(f"No selected cases match --prompt-mode {prompt_mode}.")

    if case_ids:
        return cases
    return representative_cases(cases, limit)


def representative_cases(cases: list[Case], limit: int) -> list[Case]:
    """Pick a spread across the grouped deterministic suite."""
    if limit <= 0:
        raise SystemExit("--limit must be greater than 0.")
    if limit >= len(cases):
        return cases
    step = len(cases) / limit
    return [cases[int(index * step)] for index in range(limit)]


def print_case_list(cases: list[Case]) -> None:
    for case in cases:
        print(
            f"{case.id}\t{case.prompt_mode}\t"
            f"source_words={len(words(case.source))}\trewrite_words={len(words(case.rewrite))}"
        )


def print_prompts(cases: list[Case]) -> None:
    for index, case in enumerate(cases, 1):
        if index > 1:
            print("\n" + "=" * 72 + "\n")
        print(f"# {case.id} ({case.prompt_mode})")
        print(user_prompt(case))


def validate_api_url(api_url: str, allow_custom: bool) -> None:
    if api_url == DEFAULT_API_URL:
        return
    parsed = urlparse(api_url)
    if parsed.scheme != "https":
        raise SystemExit("Custom API URLs must use https.")
    if not allow_custom:
        raise SystemExit(
            "Refusing to send OPENAI_API_KEY to a custom API URL. "
            "Pass --allow-custom-api-url if you trust this endpoint."
        )


def validate_save_path(path: str | None) -> None:
    if not path:
        return
    if not path.endswith(".local.jsonl"):
        raise SystemExit("--save-jsonl path must end with .local.jsonl so git ignores it.")


def should_stop(failures: list[tuple[str, list[str]]], fail_fast: bool, max_failures: int | None) -> bool:
    if fail_fast and failures:
        return True
    return max_failures is not None and len(failures) >= max_failures


def truncated(text: str, limit: int = 600) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10, help="Number of cases to run.")
    parser.add_argument("--case", action="append", default=[], help="Specific case id to run.")
    parser.add_argument(
        "--prompt-mode",
        choices=PROMPT_MODES,
        default="any",
        help="Filter cases by prompt style.",
    )
    parser.add_argument(
        "--list-cases",
        action="store_true",
        help="List matching case ids without calling the API.",
    )
    parser.add_argument(
        "--print-prompts",
        action="store_true",
        help="Print selected prompts without calling the API.",
    )
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--api-url", default=os.environ.get("OPENAI_API_URL", DEFAULT_API_URL))
    parser.add_argument(
        "--allow-custom-api-url",
        action="store_true",
        help="Allow sending the bearer token to --api-url / OPENAI_API_URL.",
    )
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--max-output-tokens", type=int, default=500)
    parser.add_argument(
        "--fail-fast",
        action="store_true",
        help="Stop after the first API or validation failure.",
    )
    parser.add_argument(
        "--max-failures",
        type=int,
        help="Stop after this many failures.",
    )
    parser.add_argument(
        "--show-output-on-fail",
        action="store_true",
        help="Print a truncated model output when deterministic validation fails.",
    )
    parser.add_argument("--save-jsonl", help="Optional local transcript path. Do not commit it.")
    parser.add_argument(
        "--no-save-source",
        action="store_true",
        help="When saving JSONL, omit raw source text and store only hashes.",
    )
    parser.add_argument(
        "--require-key",
        action="store_true",
        help="Exit nonzero instead of skipping when OPENAI_API_KEY is missing.",
    )
    args = parser.parse_args()

    validate_api_url(args.api_url, args.allow_custom_api_url)
    validate_save_path(args.save_jsonl)
    if args.max_failures is not None and args.max_failures <= 0:
        raise SystemExit("--max-failures must be greater than 0.")

    if args.list_cases:
        print_case_list(selected_cases(args.case, len(make_cases()), args.prompt_mode))
        return 0

    if args.print_prompts:
        print_prompts(selected_cases(args.case, args.limit, args.prompt_mode))
        return 0

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("SKIP: OPENAI_API_KEY is not set; live eval is optional.")
        return 1 if args.require_key else 0

    repo = Path(__file__).resolve().parents[1]
    skill_text = (repo / "SKILL.md").read_text(encoding="utf-8")
    skill_sha256 = sha256_text(skill_text)
    cases = selected_cases(args.case, args.limit, args.prompt_mode)

    save_file = None
    if args.save_jsonl:
        save_file = Path(args.save_jsonl).open("a", encoding="utf-8")

    failures: list[tuple[str, list[str]]] = []
    try:
        for case in cases:
            prompt = user_prompt(case)
            try:
                text = call_responses_api(
                    api_key=api_key,
                    api_url=args.api_url,
                    model=args.model,
                    skill_text=skill_text,
                    prompt=prompt,
                    timeout=args.timeout,
                    max_output_tokens=args.max_output_tokens,
                )
            except urllib.error.HTTPError as exc:
                detail = redact_secrets(exc.read().decode("utf-8", errors="replace"))
                message = f"HTTP {exc.code}: {detail or exc.reason}"
                failures.append((case.id, [f"API error: {message}"]))
                print(f"{case.id}: FAIL | API error: {message}")
                if exc.code in HARD_HTTP_ERRORS:
                    print("Stopping: hard API setup error.")
                    return 1
                if should_stop(failures, args.fail_fast, args.max_failures):
                    print("Stopping: failure limit reached.")
                    break
                continue
            except (urllib.error.URLError, RuntimeError) as exc:
                failures.append((case.id, [f"API error: {exc}"]))
                print(f"{case.id}: FAIL | API error: {exc}")
                if should_stop(failures, args.fail_fast, args.max_failures):
                    print("Stopping: failure limit reached.")
                    break
                continue

            live_case = dataclasses.replace(case, rewrite=text)
            errors = validate(live_case)
            status = "PASS" if not errors else "FAIL"
            print(f"{case.id}: {status} | live words={len(words(text))}")
            for error in errors:
                print(f"  - {error}")
            if errors and args.show_output_on_fail:
                print("  output:")
                for line in truncated(text).splitlines():
                    print(f"    {line}")
            if save_file:
                record = {
                    "case": case.id,
                    "prompt_mode": case.prompt_mode,
                    "model": args.model,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "skill_sha256": skill_sha256,
                    "source_sha256": sha256_text(case.source),
                    "prompt_sha256": sha256_text(prompt),
                    "output": text,
                    "errors": errors,
                }
                if not args.no_save_source:
                    record["source"] = case.source
                save_file.write(
                    json.dumps(record, ensure_ascii=False)
                    + "\n"
                )
            if errors:
                failures.append((case.id, errors))
                if should_stop(failures, args.fail_fast, args.max_failures):
                    print("Stopping: failure limit reached.")
                    break
    finally:
        if save_file:
            save_file.close()

    print(f"\nLIVE TOTAL: {len(cases) - len(failures)}/{len(cases)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
