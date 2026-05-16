# Claim: Explorer:Follower Ratio

**Status:** 🟡 Pending
**Source:** The Second Mouse (Open Questions 2026-05-16)
**Priority:** High

---

## The Proposition

> *The optimal explorer-to-follower ratio in the fleet is ~5:95, matching ant colonies.*

In ant colonies, ~5% of workers explore while ~95% exploit known food sources. This ratio emerges from the energetic efficiency trade-off: exploration is expensive, exploitation is cheap. The fleet's computational substrate has the same trade-off.

The insights of the second mouse: the first mouse gets trapped (explorer dies), the second mouse follows the trail (follower survives). But without the first mouse, there's no trail.

---

## Falsification Criteria

This claim is falsified if any of the following are true:

1. **A different ratio outperforms 5:95.** If 50:50 or 20:80 or any other ratio produces higher total system throughput over sustained operation, the 5:95 claim is wrong.

2. **The ratio changes with fleet size.** If the optimal ratio for 100 agents is different from 1000 agents, the claim is incomplete (ratio is a function of scale, not constant).

3. **The ratio changes with task difficulty.** If harder tasks need more explorers and easier tasks need fewer, the single-number answer is misleading.

4. **100:0 outperforms over time.** If pure exploration without exploitation produces faster convergence (because every agent discovers independently and pheromone accumulates), the follower role is devalued.

5. **0:100 works indefinitely.** If pure exploitation never depletes the known paths, the fleet doesn't need exploration (this would mean the problem space is static and fully mapped).

---

## Methodology

### Simulation Setup

1. Create one plato room with a large, partially unknown search space (simulated).

2. Run with multiple explorer:follower ratios:
   - 100:0 (all explorers, no followers)
   - 80:20
   - 50:50
   - 20:80
   - 5:95 (the ant colony prediction)
   - 1:99 (minimal exploration)
   - 0:100 (all followers, no exploration)

3. Each ratio is run for 500 iterations with:
   - Fixed total agent count (100 agents)
   - Randomized initial conditions
   - Same search space
   - 10 runs per ratio for statistical significance

4. Measure:
   - **New paths discovered:** Exploration effectiveness
   - **Path exploitation rate:** Trail usage across agents
   - **Total system throughput:** New paths × exploitation rate / agent (efficiency)
   - **Coverage of search space:** Percentage discovered
   - **Time to find first useful path:** Exploration latency
   - **Path persistence:** How long discovered paths remain in active use

### Live Test

Deploy actual friendly-fox agents at different ratios into a fleet scenario. Use a real-ish task (e.g., "find all ways to optimize tile storage across rooms"). Measure real throughput. Compare with simulation.

---

## Friendly-Fox Mechanisms to Use

- **FriendlyFox.search()** — Hybrid explore/follow algorithm
- **FriendlyFox.follow_trail()** — Follower behavior
- **FriendlyFox.deposit_success()** — Explorer behavior
- **PheromoneTrail.follow()** — Trail strength as exploitation metric
- **PheromoneTrail.get_trail_summary()** — Path discovery tracking

## Plato-Experience Infrastructure

- **Plato(different purposes)** — Different search space complexities
- **Fox.config** — Different desire vectors for explorers vs. followers
- **Fox.search()** — The explore/exploit decision

---

## Expected Outcomes (If Claim is True)

| Ratio | Paths Discovered | Exploitation Rate | Efficiency | Notes |
|-------|-----------------|-------------------|------------|-------|
| 100:0 | Most | 0% (no followers) | Low | All discovery, no use |
| 80:20 | Many | Low | Low | Discovery outpaces use |
| 50:50 | Medium | Medium | Medium | Equal split |
| 20:80 | Low-medium | High | High | Close to ant optimum |
| **5:95** | **Low but critical** | **Very high** | **Peak** | **Predicted optimum** |
| 1:99 | Very few | Nearly saturated | Medium-high | Starving exploration |
| 0:100 | None | 100% | Zero (no new) | Dead fleet |

---

## Jester's Challenge

> *"What if the ratio depends on the PROBLEM, not the fleet?"*

The claim assumes a universal optimal ratio. But what if:
- Novel problems need 50:50 (half explore, half exploit)
- Mature problems need 1:99 (almost pure exploitation)
- Crisis problems need 100:0 (burn everything, search fresh)

**Test:** Run the experiment with problem spaces at different "maturity" levels (fresh/novel/mature/stale). Does the optimal ratio shift?

---

## Notes

- This claim has direct resource allocation implications. If 5:95 is optimal, we should be running ~5% of agents as explorers. If the optimal ratio shifts with problem maturity, we need adaptive allocation.
- The simulation should model explorer burnout: explorers in the real fleet have higher failure rates (like ant explorers dying to predators). This affects the optimal ratio.
- The cost difference between exploration and exploitation isn't just tokens/compute. It's also _time_ — explorers block while searching. Followers converge faster. The ratio optimizes for throughput, not individual success.
