#!/usr/bin/env python3

from __future__ import annotations

import argparse
import collections
import json
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--period", required=True)
    parser.add_argument("--log-opts", required=True)
    parser.add_argument("--summary", required=True)
    args = parser.parse_args()

    runner_temp = Path(os.environ.get("RUNNER_TEMP", "/tmp"))
    report_path = runner_temp / f"gitleaks-{args.period}.json"
    summary_path = Path(args.summary)
    summary_path.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{os.environ['GITHUB_WORKSPACE']}:/repo",
        "-v",
        f"{runner_temp}:/reports",
        "ghcr.io/gitleaks/gitleaks:v8.30.1",
        "git",
        "/repo",
        f"--log-opts={args.log_opts}",
        "--redact=100",
        "--no-banner",
        "--no-color",
        "--log-level=error",
        "--report-format=json",
        f"--report-path=/reports/{report_path.name}",
        "--timeout=1200",
    ]

    completed = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )

    findings: list[dict[str, object]] = []
    report_parse_error = False
    if report_path.is_file() and report_path.stat().st_size:
        try:
            loaded = json.loads(report_path.read_text(encoding="utf-8"))
            if isinstance(loaded, list):
                findings = [item for item in loaded if isinstance(item, dict)]
            else:
                report_parse_error = True
        except (json.JSONDecodeError, OSError):
            report_parse_error = True

    rule_counts = collections.Counter(
        str(finding.get("RuleID", "unknown")) for finding in findings
    )

    if report_parse_error:
        status = "scanner-error"
    elif findings:
        status = "findings"
    elif completed.returncode == 0:
        status = "passed"
    else:
        status = "scanner-error"

    safe_summary = {
        "period": args.period,
        "status": status,
        "suspected_findings": len(findings),
        "rule_counts": dict(sorted(rule_counts.items())),
    }
    summary_path.write_text(
        json.dumps(safe_summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    try:
        report_path.unlink(missing_ok=True)
    except OSError:
        pass

    print(
        f"Secret scan {status} for {args.period}: "
        f"{len(findings)} suspected finding(s); values and locations suppressed."
    )
    return 0 if status == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())
