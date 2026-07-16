#!/usr/bin/env python3

from __future__ import annotations

import argparse
import collections
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def run(*args: str, cwd: Path | None = None) -> list[str]:
    completed = subprocess.run(
        list(args),
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in completed.stdout.splitlines() if line]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--period", required=True)
    parser.add_argument("--since", required=True)
    parser.add_argument("--until", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--restricted-locations", required=True)
    args = parser.parse_args()

    repository = Path(os.environ["GITHUB_WORKSPACE"])
    runner_temp = Path(os.environ.get("RUNNER_TEMP", "/tmp"))
    worktree = runner_temp / f"snapshot-scan-{args.period}"
    reports = runner_temp / f"snapshot-reports-{args.period}"
    reports.mkdir(parents=True, exist_ok=True)

    commits = run(
        "git",
        "rev-list",
        "--all",
        f"--since={args.since}",
        f"--until={args.until}",
        cwd=repository,
    )
    commits = list(dict.fromkeys(commits))

    findings: list[dict[str, object]] = []
    scanner_error = False

    if commits:
        run("git", "worktree", "add", "--detach", str(worktree), commits[0], cwd=repository)
        try:
            for index, commit in enumerate(commits):
                if index:
                    subprocess.run(
                        ["git", "checkout", "--detach", "--force", commit],
                        cwd=worktree,
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )
                    subprocess.run(
                        ["git", "clean", "-ffdqx"],
                        cwd=worktree,
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                    )

                report = reports / f"{index}.json"
                completed = subprocess.run(
                    [
                        "docker",
                        "run",
                        "--rm",
                        "-v",
                        f"{worktree}:/repo:ro",
                        "-v",
                        f"{reports}:/reports",
                        "ghcr.io/gitleaks/gitleaks:v8.30.1",
                        "dir",
                        "/repo",
                        "--redact=100",
                        "--no-banner",
                        "--no-color",
                        "--log-level=error",
                        "--report-format=json",
                        f"--report-path=/reports/{report.name}",
                        "--timeout=300",
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    check=False,
                )

                commit_findings: list[dict[str, object]] = []
                if report.is_file() and report.stat().st_size:
                    try:
                        loaded = json.loads(report.read_text(encoding="utf-8"))
                        if isinstance(loaded, list):
                            commit_findings = [
                                item for item in loaded if isinstance(item, dict)
                            ]
                    except (json.JSONDecodeError, OSError):
                        scanner_error = True

                if completed.returncode not in (0, 1):
                    scanner_error = True

                for finding in commit_findings:
                    findings.append(
                        {
                            "commit": commit,
                            "end_line": finding.get("EndLine"),
                            "file": str(finding.get("File", "")),
                            "period": args.period,
                            "rule_id": str(finding.get("RuleID", "unknown")),
                            "start_line": finding.get("StartLine"),
                        }
                    )
                report.unlink(missing_ok=True)
        finally:
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(worktree)],
                cwd=repository,
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            shutil.rmtree(worktree, ignore_errors=True)

    unique: dict[tuple[object, ...], dict[str, object]] = {}
    for finding in findings:
        key = (
            finding["commit"],
            finding["file"],
            finding["start_line"],
            finding["end_line"],
            finding["rule_id"],
        )
        unique[key] = finding
    findings = list(unique.values())

    rule_counts = collections.Counter(
        str(finding["rule_id"]) for finding in findings
    )
    if scanner_error:
        status = "scanner-error"
    elif findings:
        status = "findings"
    else:
        status = "passed"

    summary_path = Path(args.summary)
    restricted_path = Path(args.restricted_locations)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    restricted_path.parent.mkdir(parents=True, exist_ok=True)

    summary_path.write_text(
        json.dumps(
            {
                "commits_scanned": len(commits),
                "period": args.period,
                "rule_counts": dict(sorted(rule_counts.items())),
                "status": status,
                "suspected_findings": len(findings),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    restricted_path.write_text(
        json.dumps(findings, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(
        f"Snapshot scan {status} for {args.period}: "
        f"{len(commits)} commit(s), {len(findings)} suspected finding(s); "
        "values and locations suppressed."
    )
    return 0 if status != "scanner-error" else 1


if __name__ == "__main__":
    sys.exit(main())
