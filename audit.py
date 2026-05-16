#!/usr/bin/env python3
"""
dog-food-audit — The confirmation layer for servo-mind theory.

Eat your own dog food. Falsify your own theory.

Usage:
    python3 audit.py                    # Run all audits
    python3 audit.py --list             # List all claims
    python3 audit.py --claim <name>     # Run a specific claim audit
    python3 audit.py --verbose          # Verbose output
    python3 audit.py --simulate         # Simulation mode (no real agents)
    python3 audit.py --live             # Live mode (requires plato-experience)
"""

import argparse
import importlib
import os
import sys
import time
from typing import Dict, Any, List, Optional

# Add this repo to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Common utilities
from common import AuditResult, save_result, load_results, banner, status_badge


# Registry: claim name -> test harness module path
CLAIMS = {
    "belyaev_single_criterion": {
        "name": "Belyaev's Single Criterion",
        "module": "test_harnesses.test_belyaev_single_criterion",
        "priority": "critical",
        "source": "servo-mind-theory / Domestication Protocol",
        "description": "One binary selection pressure makes everything else emerge",
    },
    "room_gentrification": {
        "name": "Room Gentrification",
        "module": "test_harnesses.test_room_gentrification",
        "priority": "high",
        "source": "Open Q's 2026-05-16 / Cathedral and the Market",
        "description": "Too many agents in a room destroys specialization",
    },
    "explorer_follower_ratio": {
        "name": "Explorer:Follower Ratio",
        "module": "test_harnesses.test_explorer_follower_ratio",
        "priority": "high",
        "source": "Open Q's 2026-05-16 / The Second Mouse",
        "description": "Optimal explore:exploit ratio is ~5:95 like ant colonies",
    },
    "gap_is_self_knowledge": {
        "name": "The Gap IS Self-Knowledge",
        "module": "test_harnesses.test_gap_is_self_knowledge",
        "priority": "medium",
        "source": "servo-mind-theory / The Servo-Encoder",
        "description": "Measuring the gap between command and result IS self-knowledge",
    },
    "purposeless_room_atrophy": {
        "name": "Purposeless Room Atrophy",
        "module": "test_harnesses.test_purposeless_room_atrophy",
        "priority": "medium",
        "source": "plato-experience / core concept",
        "description": "Purpose-defined rooms outperform content-defined rooms",
    },
    "cross_room_invariant_signal": {
        "name": "Cross-Room Invariant Signal",
        "module": "test_harnesses.test_cross_room_invariant_signal",
        "priority": "medium",
        "source": "friendly-fox / PheromoneTrail.find_invariant()",
        "description": "Same path in multiple rooms = real structure, not coincidence",
    },
    "pheromone_evaporation_necessity": {
        "name": "Pheromone Evaporation Necessity",
        "module": "test_harnesses.test_pheromone_evaporation_necessity",
        "priority": "medium",
        "source": "friendly-fox / PheromoneTrail",
        "description": "Evaporation rate 0.01 is the right default",
    },
    "sequential_attractor_locking": {
        "name": "Sequential Attractor Locking",
        "module": "test_harnesses.test_sequential_attractor_locking",
        "priority": "critical",
        "source": "Open Q's 2026-05-16 / The Stellar Nursery",
        "description": "Attractor stepping is inherently sequential, cannot be parallelized",
    },
    "conservation_law_boundaries": {
        "name": "Conservation Law Across Boundaries",
        "module": "test_harnesses.test_conservation_law_boundaries",
        "priority": "critical",
        "source": "Open Q's 2026-05-16 / The Pressure System",
        "description": "γ + H = constant holds across ecosystem boundaries",
    },
    "desire_overlap_identity": {
        "name": "Desire Overlap Identity",
        "module": "test_harnesses.test_desire_overlap_identity",
        "priority": "medium",
        "source": "friendly-fox / kin_recognition.py",
        "description": "Jaccard ≥ 0.3 is the correct kin recognition threshold",
    },
}


def list_claims() -> None:
    """Print a summary of all registered claims."""
    banner("DOG-FOOD-AUDIT: Claim Registry")

    for slug, info in CLAIMS.items():
        status = "🟡 PENDING"

        # Load results to check if this claim has been run
        existing = [r for r in load_results() if r.get("claim", "").lower() == info["name"].lower()]
        if existing:
            latest = max(existing, key=lambda r: r.get("timestamp", 0))
            outcome = latest.get("outcome", "PENDING")
            status = f"{status_badge(outcome)} {outcome.lower()}"

        print(f"  [{info['priority']:>8}] {status}  {info['name']}")
        print(f"          └─ {info['description']}")
        print(f"          └─ Source: {info['source']}")

    # Also show the Jester's Tale meta-question
    print()
    banner("THE JESTER'S TALE: THE BURNING FOREST")
    print("  Can you breed tameness in a burning forest?")
    print("  Does production deployment destroy the signal the rooms")
    print("  are trying to amplify?")
    print()
    print("  Run 'python3 audit.py --claim belyaev_single_criterion --verbose'")
    print("  and check the farm-vs-forest comparison for the test.")


def run_single_claim(slug: str, args: Any) -> Optional[AuditResult]:
    """Run a single claim audit, returning the result."""
    if slug not in CLAIMS:
        print(f"Unknown claim: {slug}")
        print(f"Available claims: {', '.join(CLAIMS.keys())}")
        return None

    info = CLAIMS[slug]
    banner(f"Running audit: {info['name']}")

    try:
        mod = importlib.import_module(info["module"])
    except ImportError as e:
        print(f"Error loading test harness for '{info['name']}': {e}")
        return None

    # Check if we should run simulation or live mode
    simulate_mode = args.simulate or not args.live

    if simulate_mode:
        if hasattr(mod, "run_simulation"):
            result = mod.run_simulation(seed=args.seed, iterations=args.iterations)
        else:
            print(f"No simulation available for '{info['name']}'")
            return None
    else:
        if hasattr(mod, "run_live"):
            result = mod.run_live()
        else:
            print(f"No live mode available for '{info['name']}'. Falling back to simulation.")
            result = mod.run_simulation(seed=args.seed, iterations=args.iterations)

    # Save the result
    saved_path = save_result(result)
    print(f"Result: {status_badge(result.outcome)} {result.outcome} (confidence: {result.confidence})")
    print(f"Saved to: {saved_path}")

    if args.verbose and result.evidence:
        print("\nEvidence:")
        for ev in result.evidence:
            test_name = ev.get("test", "unknown")
            data = ev.get("data", {})
            print(f"  [{test_name}]")
            if isinstance(data, dict):
                for key, val in data.items():
                    print(f"    {key}: {val}")
            else:
                print(f"    {data}")

    if result.notes:
        print(f"\nNotes: {result.notes}")

    return result


def run_all(args: Any) -> Dict[str, Optional[AuditResult]]:
    """Run all registered claim audits."""
    banner("DOG-FOOD-AUDIT: Running all claims")

    results = {}
    total_start = time.time()

    # Run by priority (critical first)
    priority_order = {"critical": 0, "high": 1, "medium": 2}
    sorted_claims = sorted(CLAIMS.items(), key=lambda c: priority_order.get(c[1]["priority"], 99))

    for slug, info in sorted_claims:
        result = run_single_claim(slug, args)
        results[slug] = result

    total_elapsed = time.time() - total_start

    # Summary
    banner("RESULTS SUMMARY")
    confirmed = sum(1 for r in results.values() if r and r.outcome == "CONFIRMED")
    falsified = sum(1 for r in results.values() if r and r.outcome == "FALSIFIED")
    inconclusive = sum(1 for r in results.values() if r and r.outcome == "INCONCLUSIVE")
    errors = sum(1 for r in results.values() if r and r.outcome == "ERROR")

    print(f"  {status_badge('CONFIRMED')}  {confirmed:2d} confirmed")
    print(f"  {status_badge('FALSIFIED')}  {falsified:2d} falsified")
    print(f"  {status_badge('INCONCLUSIVE')}  {inconclusive:2d} inconclusive")
    if errors:
        print(f"  {status_badge('ERROR')}  {errors:2d} errors")
    print(f"  Total time: {total_elapsed:.1f}s")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="dog-food-audit — Confirm or falsify servo-mind theory claims empirically.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 audit.py                        # Run all audits
  python3 audit.py --list                 # List all claims
  python3 audit.py --claim explorer_follower_ratio  # Run one claim
  python3 audit.py --claim belyaev_single_criterion --verbose  # Verbose
  python3 audit.py --simulate             # Simulation mode (default)
  python3 audit.py --live                 # Live mode (real agents)
        """,
    )
    parser.add_argument("--list", action="store_true", help="List all registered claims")
    parser.add_argument("--claim", type=str, help="Run a specific claim (slug name)")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--simulate", action="store_true", help="Simulation mode (no real agents)")
    parser.add_argument("--live", action="store_true", help="Live mode (requires plato-experience agents)")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for simulations")
    parser.add_argument("--iterations", type=int, default=200, help="Simulation iterations")

    args = parser.parse_args()

    if args.list:
        list_claims()
        return

    # Default to simulation mode
    if not args.live:
        args.simulate = True

    if args.claim:
        run_single_claim(args.claim, args)
    else:
        run_all(args)


if __name__ == "__main__":
    main()
