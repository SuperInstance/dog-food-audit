"""
Common utilities for dog-food-audit test harnesses.

Shared helpers for:
- Running simulation experiments
- Recording results
- Loading/parsing claim definitions
- Reporting outcomes
"""

import json
import time
import os
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class AuditResult:
    """Result of running an audit on a single claim."""
    claim_name: str
    outcome: str  # "CONFIRMED", "FALSIFIED", "INCONCLUSIVE"
    confidence: float  # 0.0 to 1.0
    evidence: List[Dict[str, Any]] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "claim": self.claim_name,
            "outcome": self.outcome,
            "confidence": self.confidence,
            "evidence": self.evidence,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
            "notes": self.notes,
        }


def save_result(result: AuditResult, results_dir: str = "results") -> str:
    """Save an audit result to a JSON file. Returns the file path."""
    timestamp_str = time.strftime("%Y%m%d_%H%M%S", time.gmtime(result.timestamp))
    claim_slug = result.claim_name.lower().replace(" ", "_").replace("-", "_")
    os.makedirs(f"{results_dir}/{timestamp_str}", exist_ok=True)

    path = f"{results_dir}/{timestamp_str}/{claim_slug}.json"
    with open(path, "w") as f:
        json.dump(result.to_dict(), f, indent=2)
    return path


def load_results(results_dir: str = "results") -> List[Dict[str, Any]]:
    """Load all saved audit results."""
    results = []
    if not os.path.exists(results_dir):
        return results

    for run_dir in sorted(os.listdir(results_dir)):
        run_path = os.path.join(results_dir, run_dir)
        if not os.path.isdir(run_path):
            continue
        for fname in os.listdir(run_path):
            if fname.endswith(".json"):
                with open(os.path.join(run_path, fname)) as f:
                    results.append(json.load(f))
    return results


def banner(text: str) -> None:
    """Print a banner for visual separation in output."""
    print(f"\n{'=' * 70}")
    print(f"  {text}")
    print(f"{'=' * 70}\n")


def status_badge(status: str) -> str:
    """Return an emoji badge for a result status."""
    badges = {
        "CONFIRMED": "✅",
        "FALSIFIED": "❌",
        "INCONCLUSIVE": "🟡",
        "PENDING": "🟡",
        "ERROR": "💥",
    }
    return badges.get(status, "❓")
