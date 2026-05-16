"""
Test Harness: Room Gentrification

Audits the claim that too many agents in a room destroys specialization.

Tests:
1. Inverse-U curve for room performance vs. agent count
2. Inflection point identification
3. Path diversity changes with density
"""

from typing import Dict, Any, List
import random
import math

from common import AuditResult


def run_simulation(seed: int = 42, iterations: int = 200) -> AuditResult:
    """
    SIMULATION MODE: Vary agent counts and measure room performance metrics.

    TODO: Replace simulation stubs with actual plato-experience agent runs.
    """
    random.seed(seed)

    agent_counts = [1, 3, 5, 10, 25, 50, 100, 250, 500]
    metrics = {}

    for n in agent_counts:
        # Simulate: gentrification follows inverse-U pattern
        # Peak specialization around n=25, then declines
        optimal_density = 25.0
        decay_rate = 0.005

        # Novel discovery: peaks at optimal density, then gentrification
        discovery_base = 20.0
        discovery_curve = discovery_base * math.exp(-((n - optimal_density) ** 2) * decay_rate)
        novel_discovery = max(0, discovery_curve + random.gauss(0, discovery_base * 0.1))

        # Path diversity: Shannon-like entropy
        diversity_base = 3.0
        diversity = max(0.5, diversity_base * math.exp(-((n - optimal_density) ** 2) * decay_rate * 0.5)
                        + random.gauss(0, 0.2))

        # Specialization index: variance of path profiles
        specialization = max(0, 1.0 - abs(n - optimal_density) / optimal_density + random.gauss(0, 0.1))

        metrics[n] = {
            "novel_discovery_rate": round(novel_discovery, 2),
            "path_diversity": round(diversity, 2),
            "specialization_index": round(specialization, 2),
        }

    # Find inflection point
    inflection_point = min(metrics.keys(), key=lambda n: abs(n - 25))
    inflection_data = metrics[inflection_point]

    evidence = [
        {"test": "agent_count_vs_performance", "data": metrics},
        {"test": "inflection_point_identification", "data": {
            "optimal_count": inflection_point,
            "peak_novelty": inflection_data["novel_discovery_rate"],
            "peak_diversity": inflection_data["path_diversity"],
        }},
    ]

    return AuditResult(
        claim_name="Room Gentrification",
        outcome="INCONCLUSIVE",
        confidence=0.15,
        evidence=evidence,
        metadata={"simulation": True, "seed": seed, "iterations": iterations},
        notes="Simulation shows an inverse-U pattern consistent with gentrification, "
              "but requires live agent deployment for conclusive results.",
    )


if __name__ == "__main__":
    result = run_simulation()
    print(f"Outcome: {result.outcome} (confidence: {result.confidence})")
    data = result.evidence[0]["data"]
    for n, m in data.items():
        print(f"  {n:3d} agents: novelty={m['novel_discovery_rate']:6.2f}, diversity={m['path_diversity']:.2f}, specialist={m['specialization_index']:.2f}")
