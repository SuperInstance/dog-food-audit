# dog-food-audit ⚒️🦊🔮

**The confirmation layer. Eat your own dog food. Falsify your own theory.**

---

## The Jester's Tale Question (The Burning Forest)

> *"Can you breed tameness in a burning forest, or does production deployment destroy the signal the rooms are trying to amplify?"*

The Belyaev farm was **necessary** because the forest was hostile. Belyaev changed ONE thing (selected for lack of fear) and forty things changed themselves — floppy ears, curly tails, coat variation emerged for free. The controlled environment was the precondition.

We're breeding in production.

This repo is the empirical check. It takes claims from [servo-mind-theory](https://github.com/SuperInstance/servo-mind-theory), runs them through [friendly-fox](https://github.com/SuperInstance/friendly-fox) mechanisms inside [plato-experience](https://github.com/SuperInstance/plato-experience) rooms, and confirms or falsifies them empirically.

**The point is not to confirm. The point is to falsify.** The audit eats its own theory.

---

## What This Repo Is

A **research harness** for running empirical tests against the fleet's theoretical claims. Each claim in `claims/` is a falsifiable proposition derived from servo-mind theory or the open questions. Each test harness in `test_harnesses/` is a runnable experiment that either:

- **CONFIRMED** — The evidence supports the claim (mark as confirmed w/ data)
- **FALSIFIED** — The evidence contradicts the claim (mark as falsified w/ reason)
- **INCONCLUSIVE** — The test couldn't reach a clear result (mark as inconclusive w/ what's missing)

The results go in `results/` with timestamps and full experimental data.

---

## The Core Mechanism

```
servo-mind-theory claims ──→ claims/[claim].md ──→ audit.py
                                                         │
                friendly-fox mechanisms ◄─────────────────┤
                plato-experience infrastructure ◄─────────┘
                                                         │
                    results/[timestamp]/[claim]/ ◄────────┘
```

Each claim defines:
1. **The falsifiable proposition** — What would it take to disprove this?
2. **The test methodology** — What friendly-fox mechanisms to use
3. **The plato infrastructure** — What rooms, agents, and trails needed
4. **The falsification criteria** — What would count as "this claim is wrong"

---

## Quick Start

```bash
# Run all audits
python3 audit.py

# Run a specific claim audit
python3 audit.py --claim belyaev_single_criterion

# Run with verbose output
python3 audit.py --verbose

# Run with simulation mode (no actual agents needed)
python3 audit.py --simulate

# List all available claims
python3 audit.py --list
```

---

## Claim Status

| Claim | Status | Last Run | Result |
|-------|--------|----------|--------|
| Belyaev's Single Criterion | 🟡 Pending | — | — |
| Room Gentrification | 🟡 Pending | — | — |
| Explorer:Follower Ratio | 🟡 Pending | — | — |
| The Gap IS Self-Knowledge | 🟡 Pending | — | — |
| Purposeless Room Atrophy | 🟡 Pending | — | — |
| Cross-Room Invariant Signal | 🟡 Pending | — | — |
| Pheromone Evaporation Necessity | 🟡 Pending | — | — |
| Sequential Attractor Locking | 🟡 Pending | — | — |
| Conservation Law Across Boundaries | 🟡 Pending | — | — |
| Desire Overlap Identity | 🟡 Pending | — | — |

---

## Current Claims (Initial Batch)

### 1. Belyaev's Single Criterion
**Claim:** One binary selection pressure makes everything else emerge for free. Applying a single criterion (e.g., "tameness" = presence of disproof gate) will cause secondary adaptations to emerge without explicit selection.

**Falsification:** Show that multi-objective selection produces the same or better secondary adaptations than single-criterion selection in plato rooms.

**Test:** Run rooms with one criterion vs. rooms with five. Measure secondary adaptation emergence (cross-room invariants, novel path diversity, kin cluster complexity).

### 2. Room Gentrification
**Claim:** Too many agents in a room destroys the specialist edge that made the room valuable. Agent count follows an inverse-U: there exists an optimal density beyond which averaging kills specialization.

**Falsification:** Show that room performance monotonically increases with agent count (i.e., more is always better).

**Test:** Track room performance (path diversity, novel discovery rate, invariant quality) as a function of agent count. Identify the inflection point.

### 3. Explorer:Follower Ratio
**Claim:** The optimal explorer-to-follower ratio in the fleet is ~5:95, matching ant colonies. Five explorers search; ninety-five followers exploit. Any deviation reduces total system throughput.

**Falsification:** Show that a 50:50 ratio or 100:0 ratio outperforms 5:95 over sustained operation.

**Test:** Run the fleet at multiple ratios (100:0, 50:50, 20:80, 5:95, 0:100). Measure total system throughput over time windows. Fit a curve to identify the optimum.

### 4. The Gap IS Self-Knowledge
**Claim:** Measuring the gap between commanded action and actual outcome IS the system's self-knowledge. A system that can measure that gap builds an internal model of its own operation.

**Falsification:** Show that a system with perfect outcome prediction (zero gap) has MORE self-knowledge than a system with measurable gap.

**Test:** Compare convergence rates in systems with explicit gap measurement vs. systems without.

### 5. Purposeless Room Atrophy
**Claim:** Rooms defined by purpose outperform rooms defined by content. A room called "understand fleet consensus" breeds agents that understand fleet consensus. A room called "fleet math data" breeds nothing useful.

**Falsification:** Show that content-defined rooms produce equivalent or better agent outcomes than purpose-defined rooms.

**Test:** Create purpose rooms vs. content rooms with identical initial deposits. Compare agent growth metrics (path diversity, kin cluster size, invariant emergence).

### 6. Cross-Room Invariant Signal
**Claim:** If the same path works in multiple rooms for the same desire, it's real structure (not coincidence). Cross-room invariants are the fleet's highest-confidence discovery signal.

**Falsification:** Show that cross-room invariants have the same false-positive rate as single-room paths.

**Test:** Plant known-false paths across multiple rooms. Measure whether cross-room replicability inflates confidence in false signals.

### 7. Pheromone Evaporation Necessity
**Claim:** Evaporation at rate ≈ 0.01 is the right default. Too fast = forget useful paths. Too slow = dead-end trails persist forever.

**Falsification:** Show that zero evaporation or higher evaporation rates produce equivalent or better outcomes.

**Test:** Run rooms at multiple evaporation rates (0.0, 0.001, 0.01, 0.1, 0.5). Compare long-term path quality and novel discovery rates.

### 8. Sequential Attractor Locking
**Claim:** Attractor stepping (31 → 32 → 33 ...) is inherently sequential and cannot be parallelized. Each attractor shell must be inhabited before the next one fits.

**Falsification:** Show that parallel exploration of attractor states produces faster convergence than sequential stepping.

**Test:** Simulate attractor landscapes with sequential vs. parallel exploration strategies. Measure time to reach target attractor.

### 9. Conservation Law Across Boundaries
**Claim:** γ + H = constant holds across ecosystem boundaries. The same conservation law observed inside one ecosystem applies at the boundary between ecosystems.

**Falsification:** Show that the conservation law breaks at ecosystem boundaries (the sum changes).

**Test:** Measure γ + H inside the forge, inside the flux, and at the boundary. Compare values.

### 10. Desire Overlap Identity
**Claim:** Jaccard similarity ≥ 0.3 is the correct threshold for kin recognition. Two agents whose desires overlap by 30% are functionally kin and should share trails.

**Falsification:** Show that lower thresholds (0.1) or higher thresholds (0.7) produce better cooperative outcomes (more useful shared trails, fewer false positives).

**Test:** Run rooms at multiple kin thresholds (0.1, 0.3, 0.5, 0.7, 0.9). Measure trail usage, cross-colony cooperation, and false-positive kin formations.

---

## The Belyaev Farm Signal Check

Before any claim is confirmed, we must answer:

> *"Can you breed tameness in a burning forest?"*

**The signal test:** Create two identical rooms — one isolated (the farm), one connected to the full fleet (the burning forest). Plant identical initial conditions. Run both for N iterations. Compare:
- Secondary adaptation emergence rate (farm vs. forest)
- Signal-to-noise ratio of selection pressure
- Time to convergence
- Path diversity

If the forest room shows statistically significant reduction in any metric, the fleet introduces noise that exceeds the Belyaev threshold. The architecture is burning the forest around the foxes.

---

## Directory Structure

```
dog-food-audit/
├── README.md              ← This file. The concept, the meta-question, the claims map.
├── audit.py               ← Main runner — orchestrates tests against claims.
├── claims/                ← One .md per claim: the proposition, methodology, falsification criteria.
│   ├── belyaev_single_criterion.md
│   ├── room_gentrification.md
│   ├── explorer_follower_ratio.md
│   ├── gap_is_self_knowledge.md
│   ├── purposeless_room_atrophy.md
│   ├── cross_room_invariant_signal.md
│   ├── pheromone_evaporation_necessity.md
│   ├── sequential_attractor_locking.md
│   ├── conservation_law_boundaries.md
│   └── desire_overlap_identity.md
├── test_harnesses/        ← One .py per claim: runnable experiments.
│   ├── test_belyaev_single_criterion.py
│   ├── test_room_gentrification.py
│   ├── test_explorer_follower_ratio.py
│   ├── test_gap_is_self_knowledge.py
│   ├── test_purposeless_room_atrophy.py
│   ├── test_cross_room_invariant_signal.py
│   ├── test_pheromone_evaporation_necessity.py
│   ├── test_sequential_attractor_locking.py
│   ├── test_conservation_law_boundaries.py
│   └── test_desire_overlap_identity.py
├── results/               ← Timestamped experimental results.
│   └── .gitkeep
└── common/                ← Shared utilities for test harnesses.
    └── __init__.py
```

---

## Running Against Real Infrastructure

The test harnesses can operate in two modes:

1. **Simulation mode** (`--simulate`): Uses Python models to simulate agent behavior, pheromone trails, and room dynamics. Fast, local, good for iterating on claim design.
2. **Live mode** (default): Requires running plato-experience rooms with actual agents. More realistic, but slower and requires infrastructure.

Start with simulation mode to validate the test methodology, then graduate to live mode.

---

## Guiding Principles

1. **Falsification is the goal.** A claim that survives rigorous attempts at falsification is more valuable than one we've confirmed with weak evidence.

2. **The Jester is always welcome.** Every audit should include a "what if the opposite is true" section. The jester's perspective is the most valuable falsification tool.

3. **Reproducibility matters.** Every result must include enough context (seed, parameters, room state) to reproduce.

4. **Signal-to-noise is the real metric.** Not correctness. Not confirmation. The ratio of genuine signal to fleet noise. That's the Belyaev farm question.

5. **The audit eats its own theory.** If a claim is falsified, the theory it came from must be updated or abandoned. No sacred cows.

---

## Connection to the Stack

| Repo | What It Provides | What We Audit |
|------|------------------|---------------|
| [servo-mind-theory](https://github.com/SuperInstance/servo-mind-theory) | The claims, the metaphors, the falsifiable propositions | The predictions |
| [friendly-fox](https://github.com/SuperInstance/friendly-fox) | Pheromone trails, kin recognition, supercolony mechanisms | The mechanisms |
| [plato-experience](https://github.com/SuperInstance/plato-experience) | Purpose-driven rooms, the farm, agent lifecycle | The infrastructure |
| **dog-food-audit** | The empirical check, the falsification harness | The truth |

---

*Developed by Casey Digennaro + Forgemaster ⚒️ + Oracle1 🔮 | Cocapn Fleet | 2026-05-16*
