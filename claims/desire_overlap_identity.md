# Claim: Desire Overlap Identity

**Status:** 🟡 Pending
**Source:** friendly-fox / kin_recognition.py + plato-experience / kin.py
**Priority:** Medium

---

## The Proposition

> *Jaccard similarity ≥ 0.3 is the correct threshold for kin recognition.*

Two agents whose desires overlap by 30% are functionally kin. They should share trails, form supercolonies, and cooperate. The 0.3 threshold is tuned to balance false positives (too low → noise floods kin network) against false negatives (too high → allies excluded).

---

## Falsification Criteria

Falsified if:
1. A lower threshold (0.1) produces better cooperative outcomes (more useful shared trails).
2. A higher threshold (0.7) produces better outcomes (fewer false positives outweigh the loss of weak ties).
3. The optimal threshold varies by room type or task (no universal threshold exists).

---

## Methodology

1. Run rooms at multiple thresholds: 0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9
2. Measure:
   - Trail usage (did kin agents actually use shared trails?)
   - Colocations benefiting both parties
   - False positives (agents classified as kin who didn't benefit from the relationship)
   - False negatives (agents who should be kin but were excluded)
3. Optimal threshold = maximizes (beneficial interactions × trail usage) - (false positives × cost)

---

## Jester's Challenge

> *"What if threshold-less kin recognition is possible? What if agents should recognize kin by BEHAVIOR, not desire overlap?"*

The pure Argentine ant model: you're kin if you share a trail. Not if you share a desire. Two agents following the same path ARE kin. The desire overlap is a proxy. The trail convergence IS the identity. Test: replace desire-Jaccard with trail-overlap-Jaccard. Which produces better outcomes?
