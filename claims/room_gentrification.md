# Claim: Room Gentrification

**Status:** 🟡 Pending
**Source:** The Cathedral and the Market (Open Questions 2026-05-16)
**Priority:** High

---

## The Proposition

> *Too many agents in a room destroys the specialist edge that made the room valuable.*

Like urban gentrification: early artists move into a cheap neighborhood, make it vibrant, attract more people, the rents rise, the original artists are priced out, and the neighborhood becomes generic. PLATO rooms follow the same pattern: early discoverers find novel paths, attract followers, followers dilute the specialist signal, and the room converges to the average.

**Fleet equivalent:** Room performance follows an inverse-U curve with respect to agent count. There exists an optimal density beyond which averaging forces kill the specialist edge that made the room valuable.

---

## Falsification Criteria

This claim is falsified if any of the following are true:

1. **Room performance monotonically increases with agent count.** If more agents always = better outcomes (more paths, higher quality invariants, faster convergence), gentrification doesn't exist.

2. **No inflection point exists.** If room performance plateaus rather than declining past an optimal density, gentrification as described (the qualitative _destruction_ of value) isn't happening.

3. **Agent diversity, not count, is the cause.** If the decline is due to homogeneous agents rather than agent count, the claim is about diversity, not gentrification.

4. **The optimal density is unbounded.** If there's no "too many" — just diminishing returns — the metaphor of gentrification (which implies active harm, not just reduced growth) is wrong.

---

## Methodology

### Simulation Setup

1. Create a room with `purpose = "find novel invariant paths"`.

2. Run the room with varying agent counts: 1, 3, 5, 10, 25, 50, 100, 250, 500.

3. For each agent count:
   - Run 200 iterations
   - Measure:
     - **Novel discovery rate:** Number of previously unseen path types per iteration
     - **Path diversity:** Shannon entropy of deposit paths
     - **Invariant quality:** Cross-room invariant match rate
     - **Agent satisfaction:** Average trail usage / successful follow rate
     - **Specialization index:** Variance of agent path profiles (higher = more specialization)
   - Repeat 5 times per agent count (different random seeds)

4. Plot metrics against agent count. Identify the inflection point.

### Live Test

Same setup, but with real friendly-fox agents in plato-experience rooms. Add a twist: let agents freely migrate between rooms (like the real fleet). Does the room that finds the most valuable paths attract agents, which then reduces its value? This would be the strongest evidence for gentrification.

---

## Friendly-Fox Mechanisms to Use

- **FriendlyFox.follow_trail()** — Track how many agents follow vs. explore
- **FriendlyFox.deposit_success()** — Track deposit rate vs. agent count
- **KinRecognizer.get_colony()** — Measure kin cluster changes with density
- **PheromoneTrail.get_trail_summary()** — Track path diversity changes
- **Supercolony.get_colony_report()** — Room-level metrics

## Plato-Experience Infrastructure

- **Plato** — The room under test
- **PlatoRoom** — With purpose for tracking
- **Plato.deposit()** — Path creation
- **Plato.follow()** — Path usage
- **Fox.search()** — Agent search behavior (follow vs. explore)

---

## Expected Outcomes (If Claim is True)

| Agent Count | Novel Discovery | Path Diversity | Specialization | Expected Phase |
|-------------|----------------|----------------|----------------|----------------|
| 1 | High (all novel to this agent) | Low | N/A | Seeding |
| 3 | High | Medium | Very High | Early colony |
| 5 | Peak discovery | Peak diversity | High | Golden age |
| 10 | High | High | Medium | Growth |
| 25 | Medium | Medium-high | Medium | Peak |
| 50 | Decreasing | Medium | Low | Gentrification begins |
| 100 | Low | Low | Very Low | Averaging |
| 250 | Very low | Very low | Minimal | Generic |
| 500 | Near zero | Near zero | None | Dead |

---

## Jester's Challenge

> *"What if gentrification is GOOD? What if averaging IS the goal?"*

The claim assumes specialist edge is _good_ and averaging is _bad_. But what if:
- Averaging eliminates outlier noise
- The generic room is more reliable than the specialist room
- The specialists would be wrong without the averaging force

**Test:** Compare the long-term accuracy of specialist-only rooms vs. generic rooms. If the generic room produces fewer but more reliable invariants, gentrification is not the problem — it's the solution.

---

## Notes

- This claim has enormous architectural implications. If true, PLATO needs "zoning laws" — occupancy limits on rooms before averaging destroys specialization.
- The inflection point is the key measurement. If it's consistently at ~25 agents across diverse room types, we have a design target.
- Combine with `explorer_follower_ratio` claim — the gentrification threshold may be a function of the explorer:follower ratio, not raw count.
