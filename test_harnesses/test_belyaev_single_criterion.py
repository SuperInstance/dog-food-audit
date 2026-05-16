"""
Test Harness: Belyaev's Single Criterion

Audits the claim that ONE binary selection pressure makes everything else emerge.

Tests:
1. Multi-objective vs. single-criterion room comparison
2. Secondary adaptation emergence measurement
3. Farm (isolated) vs. forest (connected to fleet) comparison
"""

from typing import Dict, Any, List
import random

from common import AuditResult


def run_simulation(seed: int = 42, iterations: int = 500) -> AuditResult:
    """
    SIMULATION MODE: Runs rooms at different criterion counts and measures outcomes.

    TODO: Replace simulation stubs with actual plato-experience agent runs.
    """
    random.seed(seed)

    # Stub: simulate convergence rates for different criterion counts
    criterion_counts = [0, 1, 3, 5]
    results = {}

    for n_criteria in criterion_counts:
        # Simulate: primary convergence (faster = lower iterations to reach 90%)
        primary_convergence = 500 - (n_criteria * 30) + random.gauss(0, 10)

        # Simulate: secondary adaptation count
        secondary_adaptations = {
            0: random.randint(0, 3),   # No criteria: chaos
            1: random.randint(15, 30),  # Single criterion: rich emergence
            3: random.randint(8, 18),   # Three criteria: mixed
            5: random.randint(3, 10),   # Five criteria: constrained
        }

        results[n_criteria] = {
            "primary_convergence_iterations": max(1, primary_convergence),
            "secondary_adaptations": secondary_adaptations[n_criteria],
            "path_diversity": random.uniform(0.1, 0.9),
            "invariant_count": random.randint(0, 10),
        }

    # Simulate: farm vs. forest comparison
    farm_signal = results[1]["secondary_adaptations"]
    forest_secondary = max(1, farm_signal - random.randint(2, 8))  # Reduced in forest
    forest_noise_ratio = random.uniform(0.3, 0.7)

    evidence = [
        {"test": "criterion_count_comparison", "data": results},
        {"test": "farm_vs_forest", "data": {
            "farm_secondary": farm_signal,
            "forest_secondary": forest_secondary,
            "forest_noise_ratio": forest_noise_ratio,
            "signal_reduced": farm_signal - forest_secondary,
        }},
    ]

    # Tentative outcome (replace with real data)
    return AuditResult(
        claim_name="Belyaev's Single Criterion",
        outcome="INCONCLUSIVE",
        confidence=0.1,
        evidence=evidence,
        metadata={"simulation": True, "seed": seed, "iterations": iterations},
        notes="Simulation mode. Requires live agent deployment for conclusive results.",
    )


def run_live(plato_environment: Any = None) -> AuditResult:
    """
    LIVE MODE: Requires running plato-experience rooms with actual agents.

    TODO: Implement live test against plato-experience infrastructure.
    For now, falls back to simulation.
    """
    return run_simulation()


if __name__ == "__main__":
    result = run_simulation(seed=42, iterations=500)
    print(f"Outcome: {result.outcome} (confidence: {result.confidence})")
    print(f"Iterations to convergence by criterion count:")
    for n_crit, data in result.evidence[0]["data"].items():
        print(f"  {n_crit} criteria: {data['primary_convergence_iterations']:.0f} iters, {data['secondary_adaptations']} secondary adapts")
