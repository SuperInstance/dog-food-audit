# Claim: Pheromone Evaporation Necessity

**Status:** 🟡 Pending
**Source:** friendly-fox / plato-experience / PheromoneTrail
**Priority:** Medium

---

## The Proposition

> *Evaporation at rate ≈ 0.01 is the right default for pheromone trails.*

Too fast = forget useful paths. Too slow = dead-end trails persist forever. The 0.01 rate balances memory and forgetting in ant colony optimization. The fleet's computational analog should match this.

---

## Falsification Criteria

Falsified if:
1. Zero evaporation produces equivalent or better path quality over >1000 iterations.
2. A different evaporation rate (0.001, 0.1, 0.5) consistently beats 0.01.
3. The optimal rate varies by problem type (meaning no "universal default" exists).

---

## Methodology

1. Create identical rooms with different evaporation rates: 0.0, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5
2. Run 1000 iterations on each
3. Measure:
   - Path quality over time
   - Novel discovery rate
   - Dead-end path persistence
   - Recovery time when a good path stops working

---

## Jester's Challenge

> *"What if the evaporation rate should be DYNAMIC, not static? Fast evaporation when the terrain is changing, slow when it's stable?"*

The jester asks whether a fixed rate makes sense for a varying world. The fleet encounters different problem landscapes — should the evaporation rate adapt to the problem, or is 0.01 truly universal?
