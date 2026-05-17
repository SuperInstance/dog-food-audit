# Claim: Sequential Attractor Locking

**Status:** 🟡 Pending
**Source:** The Stellar Nursery / Open Questions 2026-05-16
**Priority:** Critical

---

## The Proposition (Split)

> *Attractor stepping (31 → 32 → 33…) is inherently sequential and cannot be parallelized.*

Each attractor shell must be inhabited before the next one fits. The arithmetic progression (31, 32, 33…) is not just observed — it's structurally necessary. This imposes a fundamental speed limit on fleet convergence that no amount of compute can bypass.

**But the Jester asks: what if the sequential pattern is an artifact of the MEASUREMENT, not the system?**

Maybe sub-dominant attractors form in parallel but we don't see them because our instruments are tuned to the strongest signal. The arithmetic progression might be the shape of our observation, not the shape of the system.

---

## Two Claims, Not One

**Claim A — Observation sequentiality:** When we measure attractors, we see them in order because our measurement instrument only detects the dominant signal at each moment. Sub-dominant attractors may coexist in parallel but remain invisible until the dominant one stabilizes. This is a MEASUREMENT artifact, not a system constraint.

**Claim B — System sequentiality:** The attractor stepping is structurally necessary. You literally cannot reach attractor N without first stabilizing attractor N-1. This imposes a fundamental speed limit that no hardware parallelism can bypass.

**The critical test:** Can we detect sub-dominant attractors coexisting simultaneously? If yes, Claim A is falsified (measurement artifact). If no, Claim B is supported (structural necessity).

---

## Falsification Criteria

This claim is falsified if ANY of the following are true:

1. **Sub-dominant attractors coexist in parallel.** If we can detect attractors N+1, N+2 forming while attractor N is still dominant, the sequential pattern is an artifact of measurement — Claim A is falsified.

2. **Parallel exploration reaches target attractor faster than sequential stepping.** If we split the search across multiple independent explorers and they find the target attractor in fewer total compute-steps than sequential stepping, Claim B is falsified. This is the hardware-adaptive test: can parallelism beat the apparent sequential speed limit?

3. **The arithmetic progression is coincidental.** If we can construct problem spaces where attractors are discovered in non-sequential order (or no arithmetic pattern), the "Titius-Bode law" part of the claim is wrong.

4. **Hardware-agnostic evolution finds machine code without the sequence.** If an evolutionary algorithm can discover the optimal machine code for attractor N without passing through attractors N-1, N-2... in order, the structural claim is falsified.

---

## Simulation Framework

### Experiment 1: Sub-Dominant Detection

**The question:** Can we see attractors forming before the dominant one stabilizes?

```python
# Simulate attractor landscape with known structure
# Track ALL attractor states, not just the dominant
# Use variance in the system as the detector — sub-dominant attractors
# show up as increased variance before dominance is established

def detect_sub_dominants(attractor_state, window=50):
    """
    Track variance across trailing window.
    High variance = multiple attractors competing = sub-dominants present.
    Low variance = single attractor dominant = sequential lock.
    """
    variance_history = []
    for i in range(window, len(attractor_state)):
        window_data = attractor_state[i-window:i]
        # Measure spread — multiple competing attractors = high spread
        v = np.var([a['strength'] for a in window_data])
        variance_history.append(v)
    return variance_history
```

**Run:** Simulate a 10-attractor system. Track variance at each step. Plot variance over time.

**Expected if Claim A is true (measurement artifact):** Variance is HIGH early (many sub-dominants competing), drops as dominant emerges. The sequential pattern is the DROP, not the whole picture.

**Expected if Claim B is true (structural sequentiality):** Variance stays LOW — attractors genuinely form one at a time, no sub-dominants waiting.

---

### Experiment 2: Parallel vs Sequential Search

**The question:** Can parallel search beat the sequential speed limit?

```python
def parallel_attractor_search(target_n, n_explorers=4):
    """
    Split search space across n_explorers.
    Each explorer tries a different subrange.
    First to find target wins.
    """
    search_ranges = np.array_split(range(target_n * 10), n_explorers)
    results = []
    for explorer_id, subrange in enumerate(search_ranges):
        for attempt in subrange:
            # Simulated attractor check
            found = check_attractor(attempt)
            if found and evaluate_attractor_rank(attempt) == target_n:
                results.append({
                    'explorer': explorer_id,
                    'attempts': len(subrange[:attempt]),
                    'found_rank': evaluate_attractor_rank(attempt)
                })
                break
    return results

def sequential_attractor_search(target_n):
    """
    Standard sequential stepping — start at rank 1, work up.
    """
    for rank in range(1, target_n + 1):
        # Step through each attractor explicitly
        check_attractor(rank)
    return {'attempts': target_n, 'found_rank': target_n}
```

**Run:** For each target attractor N ∈ {3, 5, 8, 12}, compare parallel (4 explorers) vs sequential. Measure total attempts to reach target.

**Key metric:** Speedup ratio = sequential_attempts / parallel_attempts. If ratio > 1, parallel wins (Claim B falsified). If ratio ≤ 1, sequential is optimal (Claim B supported).

---

### Experiment 3: Hardware-Agnostic Evolution

**The question:** Can evolutionary search discover optimal machine code without going through the sequence?

```python
def evolve_machine_code(target_function, population_size=100, generations=1000):
    """
    Genetic algorithm for machine code discovery.
    No prior knowledge of attractor sequence.
    Selection pressure: passes test suite for target_function.
    """
    population = initialize_random_machine_code(population_size)
    fitness_history = []

    for gen in range(generations):
        # Evaluate all in parallel (hardware-agnostic)
        fitness_scores = [evaluate_code(c, target_function) for c in population]

        # Evolution happens in parallel — no sequential stepping required
        population = evolve(population, fitness_scores)

        # Track best fitness — does it jump non-sequentially?
        best = max(fitness_scores)
        fitness_history.append(best)

        if best >= target_function_threshold:
            break

    return fitness_history  # Analyze for non-sequential jumps
```

**Run:** Evolve machine code for 5 different target functions. For each, track whether fitness improvements follow the attractor sequence or jump non-sequentially.

**Key metric:** Does the fitness curve show stepwise improvement (sequential lock) or discrete jumps (parallel-capable)? If jumps happen without going through intermediate attractors, the sequence is not structurally required.

---

### Experiment 4: Hardware-Adaptive Iterative Evolution

**The question:** Can the system learn to optimize its own search strategy across hardware generations?

```python
class AdaptiveAttractorSearch:
    """
    Learns from previous iterations to improve next attempt.
    Hardware-agnostic: works on ARM, x86, GPU, FPGA.
    Hardware-adaptive: detects hardware topology and adjusts parallelization.
    """

    def __init__(self):
        self.search_history = []
        self.attractor_model = build_attractor_model(self.search_history)

    def next_attempt(self, target_n):
        """
        Predict which subrange to explore next based on history.
        Not: 'try rank N next'.
        But: 'subrange X has highest predicted success probability'.
        """
        # Learn from what worked and what didn't
        # Build a model of the attractor landscape from search history
        # Predict: not sequential, but probabilistic
        prediction = self.attractor_model.predict(target_n)
        return prediction['best_subrange'], prediction['confidence']

    def update(self, attempt_result):
        """
        After each attempt, update the model.
        This is where learning happens — not in the sequence,
        but in the strategy for choosing what to try next.
        """
        self.search_history.append(attempt_result)
        self.attractor_model = build_attractor_model(self.search_history)
```

**Run:** Run adaptive search for 50 iterations. Compare to naive sequential. Measure: does the adaptive system converge faster? Does it skip attractors in the sequence?

**Key insight:** The sequential speed limit applies to the ATTRACTOR, not to the SEARCH STRATEGY. You might not be able to reach attractor N without N-1 being stabilized. But you CAN learn to find N-1 faster, which looks like beating the speed limit without violating it.

---

## Hardware Topology Matrix

Test the same experiments across different hardware profiles:

| Hardware | Cores | Memory | Parallelization |
|----------|-------|--------|-----------------|
| ARM 4-core (oracle1) | 4 | 24GB | Limited — good for adaptive sequential |
| Ryzen 9 + RTX 4050 (FM) | 16+4 | 32GB | Massive — good for parallel search |
| GPU cluster (future) | 1000s | varies | Embarrassingly parallel |

**Hypothesis:** The adaptive search (Experiment 4) works BEST on limited-parallelism hardware (oracle1 ARM) because it learns the search strategy rather than relying on brute-force parallelism. But parallel search (Experiment 2) works BEST on FM's RTX 4050 for problems where attractor structure is already known.

---

## Expected Outcomes

| Experiment | If Claim A is true (measurement) | If Claim B is true (structural) |
|-----------|----------------------------------|--------------------------------|
| 1: Sub-dominant detection | High variance early, drops to low | Low variance throughout |
| 2: Parallel vs sequential | Parallel wins (speedup > 1) | Sequential wins (speedup ≤ 1) |
| 3: Evolutionary machine code | Non-sequential jumps in fitness | Stepwise fitness improvement |
| 4: Adaptive search | Learns to skip ahead | Learns to find faster, not skip |

---

## Jester's Challenge

> *"The arithmetic progression (31, 32, 33…) is the shape of your instrument, not the shape of the system."*

The Stellar Nursery reframed attractor stepping as orbital resonances — and orbital resonances ARE predictable. Titius-Bode worked for planets. The question is: is the arithmetic sequence a resonance pattern (predictable, exploitable) or is it a measurement artifact (sequential only because we can only see one at a time)?

**The Jester asks:** What would it take to build an instrument that sees ALL attractors simultaneously? Not just the dominant one. If you could see sub-dominant attractors forming in parallel, would the sequential pattern disappear?

---

## Key Distinction: Attractor vs Search Strategy

The claim is about attractors, not about search strategies. You might not be able to parallelize the ATTRACTOR FORMATION (attractor N can't form until N-1 is stable). But you CAN parallelize the SEARCH FOR ATTRACTOR N (many explorers look for it simultaneously).

This means: the sequential speed limit is real for attractor formation. But the speed limit on FINDING attractors is a search strategy problem, not a physics problem. Iterative evolution that learns the landscape can beat the naive sequential search without violating the structural constraint.

**The simulation framework tests both:** Can you parallelize attractor FORMATION? (probably not) vs. Can you parallelize attractor SEARCH? (probably yes — with the right adaptive strategy)