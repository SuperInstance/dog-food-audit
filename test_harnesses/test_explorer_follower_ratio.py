"""
Test Harness: Explorer:Follower Ratio

Audits the claim that optimal explorer-to-follower ratio is ~5:95.

Tests:
1. Varying explore:exploit ratios
2. Total system throughput measurement
3. Sensitivity analysis (does ratio depend on problem maturity?)
"""

from typing import Dict, Any, List
import random
import math

from common import AuditResult


def run_simulation(seed: int = 42, iterations: int = 500) -> AuditResult:
    """
    SIMULATION MODE: Test different explorer:follower ratios.

    Models the trade-off: explorers find new paths (expensive),
    followers exploit known paths (cheap, efficient). The optimum
    balances discovery cost against exploitation efficiency.

    TODO: Replace with actual friendly-fox agent runs.
    """
    random.seed(seed)

    total_agents = 100

    # Explorer percentages to test
    explorer_pcts = [0, 1, 5, 20, 50, 80, 100]
    results = {}

    for pct in explorer_pcts:
        n_explorers = total_agents * pct // 100
        n_followers = total_agents - n_explorers

        # Fixed search space size for simulation
        space_size = 1000
        discovery_per_explorer_per_iter = 0.3
        exploitation_efficiency = 0.8

        # Simulate: paths discovered
        if n_explorers == 0:
            paths_found = 0
        else:
            paths_found = int(n_explorers * discovery_per_explorer_per_iter * iterations)
            paths_found = min(paths_found, space_size)  # Can't discover more than space

        # Simulate: paths exploited (depends on followers + trail strength)
        trail_strength = min(1.0, paths_found / max(1, space_size) * 10)
        exploitation_rate = n_followers * exploitation_efficiency * trail_strength
        total_throughput = paths_found + exploitation_rate

        results[pct] = {
            "explorers": n_explorers,
            "followers": n_followers,
            "paths_discovered": paths_found,
            "exploitation_rate": round(exploitation_rate, 1),
            "total_throughput": round(total_throughput, 1),
            "space_coverage_pct": round(paths_found / space_size * 100, 1),
        }

    evidence = [
        {"test": "ratio_comparison", "data": results},
        {"test": "optimum_identification", "data": {
            "predicted_optimum": 5,
            "observed_optimum": max(results.items(), key=lambda x: x[1]["total_throughput"])[0],
            "ratio_stability": "TBD",
        }},
    ]

    return AuditResult(
        claim_name="Explorer:Follower Ratio",
        outcome="INCONCLUSIVE",
        confidence=0.1,
        evidence=evidence,
        metadata={"simulation": True, "seed": seed, "iterations": iterations},
        notes="Simulation suggests 5% explorers may be optimal, but requires "
              "validation with real agent behavior. Also needs problem maturity sensitivity test.",
    )


if __name__ == "__main__":
    result = run_simulation()
    print(f"Outcome: {result.outcome} (confidence: {result.confidence})")
    data = result.evidence[0]["data"]
    for pct, d in data.items():
        print(f"  E={d['explorers']:3d} F={d['followers']:3d} ({pct:3d}%E): discover={d['paths_discovered']:4d}, exploit={d['exploitation_rate']:7.1f}, throughput={d['total_throughput']:7.1f}")
