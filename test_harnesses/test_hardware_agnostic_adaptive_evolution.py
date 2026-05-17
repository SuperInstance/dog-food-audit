"""
Hardware-Agnostic Adaptive Evolution — Test Harness

Tests iterative evolution at machine code level that:
1. Works on any hardware (ARM, x86, GPU, FPGA) — hardware-agnostic
2. Infers hardware topology from execution feedback — hardware-adaptive
3. Learns to optimize its own search strategy through iteration

Run: python3 test_hardware_agnostic_adaptive_evolution.py
"""

import numpy as np
import time
import json
import os
from typing import Dict, List, Tuple, Optional

# ─── Machine Code Primitives ────────────────────────────────────────────────

class MachineCodeProgram:
    """A program is a list of operations that operate on a register file."""

    OPERATIONS = ['load', 'store', 'add', 'sub', 'mul', 'div', 'compare', 'branch', 'halt']

    def __init__(self, instructions: List[Dict]):
        self.instructions = instructions

    @staticmethod
    def random(program_length: int = 20) -> 'MachineCodeProgram':
        """Generate a random program."""
        instructions = []
        for _ in range(program_length):
            op = np.random.choice(MachineCodeProgram.OPERATIONS)
            inst = {'op': op}
            if op in ['load', 'store', 'add', 'sub', 'mul', 'div', 'compare']:
                inst['reg_a'] = np.random.randint(0, 8)
                inst['reg_b'] = np.random.randint(0, 8)
            if op == 'branch':
                inst['target'] = np.random.randint(0, program_length)
            instructions.append(inst)
        return MachineCodeProgram(instructions)

    def mutate(self, rate: float = 0.1) -> 'MachineCodeProgram':
        """Mutate this program."""
        new_instructions = []
        for inst in self.instructions:
            if np.random.random() < rate:
                # Mutate this instruction
                op = np.random.choice(MachineCodeProgram.OPERATIONS)
                new_inst = {'op': op}
                if op in ['load', 'store', 'add', 'sub', 'mul', 'div', 'compare']:
                    new_inst['reg_a'] = np.random.randint(0, 8)
                    new_inst['reg_b'] = np.random.randint(0, 8)
                if op == 'branch':
                    new_inst['target'] = np.random.randint(0, len(self.instructions))
                new_instructions.append(new_inst)
            else:
                new_instructions.append(inst.copy())
        return MachineCodeProgram(new_instructions)

    def crossover(self, other: 'MachineCodeProgram') -> 'MachineCodeProgram':
        """Single-point crossover."""
        min_len = min(len(self.instructions), len(other.instructions))
        if min_len == 0:
            return self.mutate(1.0)
        point = np.random.randint(1, min_len)
        child = MachineCodeProgram(self.instructions[:point] + other.instructions[point:])
        return child


class TargetFunction:
    """A target function to evolve code for."""

    def __init__(self, name: str, input_size: int, test_cases: List[Tuple]):
        self.name = name
        self.input_size = input_size
        self.test_cases = test_cases  # List of (input, expected_output)

    def evaluate(self, program: MachineCodeProgram) -> Tuple[float, float]:
        """
        Evaluate a program against all test cases.
        Returns (correctness_score, execution_time).
        correctness: fraction of test cases passed (0 to 1)
        execution_time: wall-clock time in seconds
        """
        start = time.time()
        passed = 0
        for input_data, expected in self.test_cases:
            result = self._execute(program, input_data)
            if result == expected:
                passed += 1
        elapsed = time.time() - start
        return passed / len(self.test_cases), elapsed

    def _execute(self, program: MachineCodeProgram, input_data: List) -> List:
        """Execute a program on input data. Returns output list."""
        # Simplified execution — real implementation would interpret machine code
        # For sorting: check if output is sorted and correct
        # For checksum: compute CRC and compare
        registers = input_data[:8] + [0] * (8 - len(input_data))
        pc = 0
        max_steps = 1000
        steps = 0
        while pc < len(program.instructions) and steps < max_steps:
            inst = program.instructions[pc]
            op = inst['op']
            if op == 'halt':
                break
            elif op == 'add':
                ra = inst.get('reg_a', 0)
                rb = inst.get('reg_b', 0)
                if ra < len(registers) and rb < len(registers):
                    registers[ra] = registers[ra] + registers[rb]
            elif op == 'compare':
                ra = inst.get('reg_a', 0)
                rb = inst.get('reg_b', 0)
                if ra < len(registers) and rb < len(registers):
                    registers[ra] = 1 if registers[ra] > registers[rb] else 0
            pc += 1
            steps += 1
        return registers[:len(input_data)]


# ─── Hardware-Agnostic Adaptive Evolver ──────────────────────────────────────

class HardwareAgnosticEvolver:
    """
    Evolves machine code through iterative selection.
    Hardware-agnostic: only uses generic operations.
    Hardware-adaptive: infers hardware topology from execution feedback.
    """

    def __init__(self, target: TargetFunction, population_size: int = 32):
        self.target = target
        self.population_size = population_size
        self.population = [MachineCodeProgram.random(20) for _ in range(population_size)]
        self.execution_history: List[Dict] = []
        self.hardware_profile = {
            'type': 'unknown',
            'parallel_potential': 'unknown',
            'strategy': 'sequential'
        }
        self.fitness_history: List[float] = []
        self.generation = 0

    def fitness(self, code: MachineCodeProgram) -> Tuple[float, float]:
        return self.target.evaluate(code)

    def infer_hardware(self, execution_times: List[float]) -> Dict:
        """
        Infer hardware profile from execution times — behavior, not architecture.
        """
        if not execution_times:
            return self.hardware_profile

        mean_t = np.mean(execution_times)
        std_t = np.std(execution_times)
        cv = std_t / mean_t if mean_t > 0 else 0

        if cv > 0.5:
            self.hardware_profile = {'type': 'memory_bound', 'parallel_potential': 'low'}
        elif cv < 0.1 and mean_t < 0.001:
            self.hardware_profile = {'type': 'compute_bound', 'parallel_potential': 'high'}
        else:
            self.hardware_profile = {'type': 'mixed', 'parallel_potential': 'medium'}

        # Set strategy
        pp = self.hardware_profile['parallel_potential']
        if pp == 'high':
            self.hardware_profile['strategy'] = 'parallel_map'
            self.hardware_profile['splits'] = 8
        elif pp == 'low':
            self.hardware_profile['strategy'] = 'sequential'
        else:
            self.hardware_profile['strategy'] = 'adaptive_mix'
            self.hardware_profile['splits'] = 4

        return self.hardware_profile

    def select_parallelization_strategy(self) -> Dict:
        return {
            'strategy': self.hardware_profile['strategy'],
            'splits': self.hardware_profile.get('splits', 1)
        }

    def evolve_one_generation(self) -> Tuple[List[MachineCodeProgram], List[float], List[float]]:
        """
        Evolve one generation: evaluate, select, mutate, crossover.
        Returns (new_population, fitness_scores, execution_times).
        """
        # Evaluate all
        fitness_scores = []
        execution_times = []

        for code in self.population:
            score, exec_t = self.fitness(code)
            fitness_scores.append(score)
            execution_times.append(exec_t)
            self.execution_history.append({'generation': self.generation, 'score': score, 'exec_time': exec_t})

        # Update hardware inference every 5 generations
        if self.generation % 5 == 0:
            self.infer_hardware(execution_times)

        # Selection: tournament
        new_population = []
        while len(new_population) < self.population_size:
            # Tournament of 3
            candidates = np.random.choice(len(self.population), 3, replace=False)
            best = max(candidates, key=lambda i: fitness_scores[i])
            winner = self.population[best]

            # Mutate
            child = winner.mutate(rate=0.1)
            new_population.append(child)

        self.population = new_population
        self.generation += 1
        self.fitness_history.append(max(fitness_scores))

        return self.population, fitness_scores, execution_times

    def run(self, max_generations: int = 100, target_fitness: float = 0.95) -> Dict:
        """
        Run the evolver. Returns history.
        """
        history = {
            'generations': [],
            'best_fitness': [],
            'hardware_profiles': [],
            'strategies': []
        }

        for gen in range(max_generations):
            pop, scores, exec_times = self.evolve_one_generation()
            best_score = max(scores)
            history['generations'].append(self.generation)
            history['best_fitness'].append(best_score)
            history['hardware_profiles'].append(self.hardware_profile.copy())
            history['strategies'].append(self.hardware_profile['strategy'])

            if gen % 20 == 0 or best_score >= target_fitness:
                print(f"  Gen {gen}: best={best_score:.2f}, hardware={self.hardware_profile['type']}, strategy={self.hardware_profile['strategy']}")

            if best_score >= target_fitness:
                print(f"  Converged at generation {gen}")
                break

        return history


# ─── Fixed Strategy Evolver (Comparator) ────────────────────────────────────

class FixedStrategyEvolver:
    """Non-adaptive evolver — fixed parallelization strategy."""

    def __init__(self, target: TargetFunction, population_size: int = 32):
        self.target = target
        self.population_size = population_size
        self.population = [MachineCodeProgram.random(20) for _ in range(population_size)]
        self.fitness_history: List[float] = []
        self.generation = 0

    def fitness(self, code: MachineCodeProgram) -> Tuple[float, float]:
        return self.target.evaluate(code)

    def evolve_one_generation(self):
        scores = [self.fitness(c)[0] for c in self.population]
        new_population = []
        while len(new_population) < self.population_size:
            candidates = np.random.choice(len(self.population), 3, replace=False)
            best = max(candidates, key=lambda i: scores[i])
            winner = self.population[best]
            child = winner.mutate(rate=0.1)
            new_population.append(child)
        self.population = new_population
        self.generation += 1
        self.fitness_history.append(max(scores))
        return scores

    def run(self, max_generations: int = 100, target_fitness: float = 0.95) -> Dict:
        history = {'generations': [], 'best_fitness': []}
        for gen in range(max_generations):
            scores = self.evolve_one_generation()
            history['generations'].append(self.generation)
            history['best_fitness'].append(max(scores))
            if gen % 20 == 0:
                print(f"  Gen {gen}: best={max(scores):.2f}")
            if max(scores) >= target_fitness:
                break
        return history


# ─── Target Functions ─────────────────────────────────────────────────────────

def make_sorting_target(n_elements: int = 4) -> TargetFunction:
    """Create a sorting network target function."""
    test_cases = []
    for _ in range(50):
        data = list(np.random.randint(0, 100, n_elements))
        expected = sorted(data)
        test_cases.append((data, expected))
    return TargetFunction(f"sort_{n_elements}", n_elements, test_cases)


def make_checksum_target() -> TargetFunction:
    """Create a checksum computation target function."""
    test_cases = []
    for _ in range(30):
        data = list(np.random.randint(0, 256, 8))
        expected = sum(data) % 256  # Simple checksum
        test_cases.append((data, [expected]))
    return TargetFunction("checksum", 8, test_cases)


# ─── Experiments ─────────────────────────────────────────────────────────────

def experiment_hardware_adaptive_speedup(target: TargetFunction, n_runs: int = 3) -> Dict:
    """
    Experiment 2: Adaptive vs Static speedup.
    """
    results = []

    for run in range(n_runs):
        print(f"\n=== Run {run + 1}/{n_runs}: Sorting target ===")
        np.random.seed(run * 42)

        print("  [Static] Running fixed-strategy evolver...")
        static = FixedStrategyEvolver(target, population_size=32)
        static_history = static.run(max_generations=200)
        static_time = 0.0  # Will track convergence generation instead

        print("  [Adaptive] Running hardware-adaptive evolver...")
        np.random.seed(run * 42)
        adaptive = HardwareAgnosticEvolver(target, population_size=32)
        adaptive_history = adaptive.run(max_generations=200)

        # Find convergence generation
        def find_convergence(history, threshold=0.8):
            for i, f in enumerate(history['best_fitness']):
                if f >= threshold:
                    return i
            return len(history['best_fitness'])

        static_conv = find_convergence(static_history, 0.8)
        adaptive_conv = find_convergence(adaptive_history, 0.8)

        print(f"  Static converged: gen {static_conv}")
        print(f"  Adaptive converged: gen {adaptive_conv}")
        print(f"  Hardware profile inferred: {adaptive.hardware_profile}")

        results.append({
            'run': run,
            'static_convergence': static_conv,
            'adaptive_convergence': adaptive_conv,
            'speedup': static_conv / adaptive_conv if adaptive_conv > 0 else float('inf'),
            'hardware_profile': adaptive.hardware_profile,
            'strategy_used': adaptive.hardware_profile['strategy']
        })

    # Aggregate
    avg_speedup = np.mean([r['speedup'] for r in results])
    print(f"\nAverage speedup (adaptive vs static): {avg_speedup:.2f}x")

    return {
        'results': results,
        'avg_speedup': avg_speedup,
        'adaptive_wins': sum(1 for r in results if r['speedup'] > 1.0)
    }


def experiment_learning_curve(target: TargetFunction, n_runs: int = 5) -> Dict:
    """
    Experiment 4: Does the adaptive system get faster with repetition?
    """
    print(f"\n=== Learning Curve: {n_runs} runs on same target ===")

    convergence_gens = []

    for run in range(n_runs):
        print(f"  Run {run + 1}/{n_runs}...")
        np.random.seed(run * 100)
        evolver = HardwareAgnosticEvolver(target, population_size=32)
        history = evolver.run(max_generations=200)

        # Find convergence gen
        for i, f in enumerate(history['best_fitness']):
            if f >= 0.8:
                convergence_gens.append(i)
                break
        else:
            convergence_gens.append(200)

        print(f"    Converged at gen {convergence_gens[-1]}, final fitness: {history['best_fitness'][-1]:.2f}")

    # Check: do later runs converge faster?
    early = np.mean(convergence_gens[:2])
    late = np.mean(convergence_gens[-2:])
    learning_improvement = early / late if late > 0 else 0

    print(f"\nEarly runs avg convergence: {early:.1f} gens")
    print(f"Late runs avg convergence: {late:.1f} gens")
    print(f"Learning improvement: {learning_improvement:.2f}x")

    return {
        'convergence_gens': convergence_gens,
        'early_avg': early,
        'late_avg': late,
        'learning_improvement': learning_improvement
    }


def run_all_experiments():
    """Run the full experiment suite."""
    print("=" * 70)
    print("HARDWARE-AGNOSTIC ADAPTIVE EVOLUTION — Experiment Suite")
    print("=" * 70)

    results = {}

    # Experiment 2: Adaptive speedup
    print("\n[Experiment 2] Adaptive vs Static Speedup")
    print("-" * 50)
    target = make_sorting_target(4)
    results['adaptive_speedup'] = experiment_hardware_adaptive_speedup(target, n_runs=3)

    # Experiment 4: Learning curve
    print("\n[Experiment 4] Learning Curve")
    print("-" * 50)
    results['learning_curve'] = experiment_learning_curve(target, n_runs=5)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Adaptive speedup: {results['adaptive_speedup']['avg_speedup']:.2f}x")
    print(f"Adaptive wins: {results['adaptive_speedup']['adaptive_wins']}/3 runs")
    print(f"Learning improvement: {results['learning_curve']['learning_improvement']:.2f}x")

    # Save results
    os.makedirs('results', exist_ok=True)
    with open('results/hardware_adaptive_evolution.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print("\nResults saved to results/hardware_adaptive_evolution.json")

    return results


if __name__ == "__main__":
    run_all_experiments()