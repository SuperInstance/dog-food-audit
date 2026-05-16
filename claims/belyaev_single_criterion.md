# Claim: Belyaev's Single Criterion

**Status:** 🟡 Pending
**Source:** servo-mind-theory / Domestication Protocol
**Priority:** Critical

---

## The Proposition

> *One binary selection pressure makes everything else emerge for free.*

Belyaev selected for ONE trait (tameness = lack of fear response) in silver foxes and observed forty+ secondary adaptations emerge: floppy ears, curly tails, coat variation, skull shape changes, altered stress hormone levels. The controlled farm environment was necessary — the single criterion could only express in isolation.

**Fleet analog:** Selecting for a single binary criterion in PLATO rooms (e.g., "does this tile pass the DisproofOnlyGate?") will cause secondary functional adaptations to emerge without explicit multi-objective optimization.

---

## Falsification Criteria

This claim is falsified if any of the following are true:

1. **Multi-objective selection produces MORE secondary adaptations than single-criterion selection.** If running 5 criteria simultaneously produces more novel path types, broader invariants, or faster convergence than 1 criterion, the "single criterion" claim is wrong.

2. **No secondary adaptations emerge.** If running a room with only one criterion for 1000+ iterations produces zero emergent behaviors that weren't explicitly selected for, the "everything else emerges for free" part is wrong.

3. **The single criterion converges slower on the primary metric.** If the single criterion room achieves the primary goal slower than the multi-criterion room, the claim that simpler selection is more powerful is wrong.

4. **The "farm" isn't necessary.** If a room connected to the live fleet shows equivalent secondary adaptation emergence to an isolated room, the claim that controlled environments are necessary is wrong.

---

## Methodology

### Simulation Setup

1. Create 5 plato rooms with identical initial conditions:
   - **Room A (Single criterion):** Only criterion is `passes_disproof_gate`. A tile enters if it falsifies an existing tile; otherwise it's rejected.
   - **Room B (Three criteria):** `passes_disproof_gate` + `high_confidence` + `cross_room_replicate`
   - **Room C (Five criteria):** `passes_disproof_gate` + `high_confidence` + `cross_room_replicate` + `novel_path` + `kin_agreement`
   - **Room D (Control, zero criteria):** No selection. All tiles enter.
   - **Room E (Burning forest):** Single criterion, but connected to the live fleet (production noise).

2. Seed each room with the same initial 10 tiles (known truths).

3. Run for 500 iterations. Each iteration: agents deposit tiles, selection gate applies, mortality sweep prunes weak tiles.

4. Measure at each iteration:
   - **Primary metric:** Percentage of new tiles that pass the primary criterion (convergence speed)
   - **Secondary adaptations:** Tile diversity (unique path types), invariant count, kin cluster size, novel discovery rate
   - **Noise metric (Room E only):** Signal-to-noise ratio — fraction of introduced tiles that are from fleet noise vs. productive deposits

### Live Test

Set up the same 5 rooms in actual plato-experience infrastructure with real friendly-fox agents. Run for the same 500 iterations. Compare simulation vs. live results.

---

## Friendly-Fox Mechanisms to Use

- **DisproofOnlyGate** — The primary selection criterion for Room A
- **PheromoneTrail.find_invariant()** — Measure cross-room invariants as secondary adaptation
- **KinRecognizer.form_supercolony()** — Measure kin cluster complexity
- **PheromoneTrail.get_trail_summary()** — Track path diversity
- **Supercolony.get_colony_report()** — Measure colony structure changes

## Plato-Experience Infrastructure

- **PlatoRoom** — One per experimental condition (5 rooms)
- **Plato.follow()** — Trail usage tracking
- **Plato.deposit()** — Tile creation
- **Plato.evaporate()** — Mortality simulation
- **Supercolony** — Cross-room invariant tracking

---

## Expected Outcomes (If Claim is True)

| Condition | Primary Convergence | Secondary Adaptations | Noise |
|-----------|-------------------|----------------------|-------|
| Room A (1 criterion) | Fastest | Highest | N/A |
| Room B (3 criteria) | Medium | Medium | N/A |
| Room C (5 criteria) | Slowest | Lowest | N/A |
| Room D (no criteria) | Random | Structureless | N/A |
| Room E (forest) | Slower than A | Reduced vs. A | High |

---

## Jester's Challenge

> *"What if the ONE criterion isn't the right one?"*

The claim doesn't say _any_ single criterion works — it says Belyaev's criterion (lack of fear) was the right one. What if the DisproofOnlyGate isn't the fleet's equivalent of tameness? What if the real single criterion is something we haven't identified — like "contributes to a supercolony that converges on truth"?

**Test:** Repeat the experiment with different single criteria. Is there ONE that outperforms all others?

---

## Notes

- The "burning forest" test (Room E) is the Jester's Tale question. If Room E shows significantly reduced secondary adaptations, the architecture cannot breed effectively in production. This is the most important single result.
- If Room A converges slower than Room B, the claim that "one criterion is best" is falsified. But if Room A converges slower but produces RICHER secondary adaptations, the trade-off is real and the claim is partially supported.
