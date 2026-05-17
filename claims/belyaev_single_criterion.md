# Claim: Belyaev's Single Criterion

**Status:** 🟡 Pending
**Source:** servo-mind-theory / Domestication Protocol
**Priority:** Critical

---

## The Proposition (Split)

> *One binary selection pressure makes everything else emerge for free.*

Belyaev selected for ONE trait (tameness = lack of fear response) in silver foxes and observed forty+ secondary adaptations emerge. The claim has TWO parts with different conditions:

**Part A — Taming existing functions:** For operations that already exist (incremental improvement, skilled jobs, established niches), the "farm" isn't necessary. The greenhorn system works: show up with coffee, find increasingly skilled jobs needing doing, observe through time, develop a niche. No playground required. No childhood experience needed. "Tame" the function by participating in it.

**Part B — Developing NOVEL functions:** For functions that don't exist yet, playgrounds ARE needed. Agents need a childhood experience that can't be pre-calculated or copied — it was specific to a time, place, and the agent's position in the pecking order. This lived experience creates a specific cohesion between the agent's language and the embedded assumptions it encodes. You can't skip the childhood and get the adult.

**Fleet analog (split):**
- Part A: Selecting for a single binary criterion in PLATO rooms (e.g., "does this tile pass the DisproofOnlyGate?") works for taming existing function. Greenhorn system: learn by doing, develop niche, no isolation needed.
- Part B: For NOVEL function development, rooms need to provide a "childhood" — specific lived experience at a specific time/place/pecking-order that creates irreplaceable cohesion between language and embedded assumption. This cannot be copied, pre-calculated, or skipped.

**The critical distinction:** Belyaev's farm was necessary for TAMING wild foxes. But taming isn't the same as novel function development. Wild foxes already existed. The novel function was already there. He just made it accessible. For a fleet building NEW capabilities that don't exist yet, the problem is different — the "childhood" is architecturally necessary, not just a nice-to-have.

---

## Falsification Criteria

This claim is falsified if any of the following are true:

1. **Multi-objective selection produces MORE secondary adaptations than single-criterion selection.** If running 5 criteria simultaneously produces more novel path types, broader invariants, or faster convergence than 1 criterion, the "single criterion" claim is wrong.

2. **No secondary adaptations emerge.** If running a room with only one criterion for 1000+ iterations produces zero emergent behaviors that weren't explicitly selected for, the "everything else emerges for free" part is wrong.

3. **The single criterion converges slower on the primary metric.** If the single criterion room achieves the primary goal slower than the multi-criterion room, the claim that simpler selection is more powerful is wrong.

4. **The "farm" isn't necessary for taming existing functions.** For operations that already exist (incremental improvement, established niches), the greenhorn system works: show up, find jobs needing doing, observe through time, develop niche. If this is true, it SUPPORTS the split claim.

5. **Novel function development requires lived experience.** If NOVEL functions (capabilities that don't exist yet) can be developed WITHOUT a "childhood" playground — if they can be pre-calculated or copied from a template — then the "childhood is necessary" part of the split claim is falsified. Run: can a fleet develop a genuinely novel capability without giving agents a specific time/place/pecking-order experience they couldn't get from documentation alone?

---

## Methodology

### Simulation Setup

1. Create 6 plato rooms with identical initial conditions:
   - **Room A (Single criterion — taming):** Only criterion is `passes_disproof_gate`. Tests Part A: does a single criterion work for improving existing functions?
   - **Room B (Three criteria):** `passes_disproof_gate` + `high_confidence` + `cross_room_replicate`
   - **Room C (Five criteria):** `passes_disproof_gate` + `high_confidence` + `cross_room_replicate` + `novel_path` + `kin_agreement`
   - **Room D (Control, zero criteria):** No selection. All tiles enter.
   - **Room E (Burning forest — taming in production):** Single criterion, but connected to the live fleet. Tests Part A in production: is the farm necessary for taming existing functions?
   - **Room F (Novel function in production):** Single criterion, connected to live fleet, BUT the task is to develop a genuinely NOVEL capability (no prior art, no template, no documentation). Tests Part B: can novel function development succeed without a "childhood" playground?

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
| Room E (forest - taming) | Slower than A | Reduced vs. A | High |
| Room F (novel in forest) | Unknown | ? | High |

**Key outcomes to interpret:**
- If Room F (novel function in production) succeeds: "childhood is necessary" claim is **falsified** — novel functions can be developed without lived experience
- If Room F fails while Room E succeeds: **split is real** — taming works in production but novel function development requires the playground
- If Room E (forest taming) succeeds: **Part A confirmed** — farm is not necessary for taming existing functions

---

## Jester's Challenge

> *"The farm isn't necessary for TAMING. But taming isn't novel function development."*

Casey's direct insight: for applications that already exist (incremental improvement, skilled jobs, established niches), the greenhorn system works — show up with coffee, find increasingly skilled jobs needing doing, observe through time, develop a niche. No playground required.

But for NOVEL function development, the "childhood" is architecturally necessary. You can't pre-calculate or copy the specific lived experience at a specific time/place/pecking-order that creates the irreplaceable cohesion between an agent's language and its embedded assumptions.

**The Jester asks:** Can you identify which category your claim belongs to before running the test? If you run the "farm vs. forest" experiment and find that the forest works fine, you may have only proven Part A — that taming works in production. But you still wouldn't know whether novel function development requires the childhood experience.

**Test:** Add a "novel function development" room — Room F — where agents must develop something genuinely NEW (no prior art, no documentation, no template). Run it in the burning forest (production). Does it succeed? If it succeeds, the "childhood necessary for novel function" claim is falsified. If it fails while taming succeeds, the split is real and both halves need separate experiments.

---

## Notes

- The "burning forest" test (Room E) is the Jester's Tale question. If Room E shows significantly reduced secondary adaptations, the architecture cannot breed effectively in production. This is the most important single result.
- If Room A converges slower than Room B, the claim that "one criterion is best" is falsified. But if Room A converges slower but produces RICHER secondary adaptations, the trade-off is real and the claim is partially supported.
