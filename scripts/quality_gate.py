"""Fail the pipeline when a high-severity, high-confidence Bandit finding exists."""
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/quality_gate.py <bandit-report.json>")
        return 2

    report_path = Path(sys.argv[1])
    if not report_path.is_file():
        print(f"Quality Gate ERROR: report not found: {report_path}")
        return 2

    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Quality Gate ERROR: cannot read valid JSON report: {error}")
        return 2

    findings = report.get("results", [])
    blockers = [
        finding for finding in findings
        if finding.get("issue_severity") == "HIGH"
        and finding.get("issue_confidence") == "HIGH"
    ]

    print(f"Bandit findings reviewed: {len(findings)}")
    print(f"Blocking findings (HIGH severity + HIGH confidence): {len(blockers)}")
    for finding in blockers:
        print(
            f"- {finding.get('filename')}:{finding.get('line_number')} "
            f"{finding.get('test_id')} — {finding.get('issue_text')}"
        )

    if blockers:
        print("QUALITY GATE: FAILED")
        return 1

    print("QUALITY GATE: PASSED under the configured policy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
