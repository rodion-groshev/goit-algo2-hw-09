import random
import math


def generate_neighbor(solution, bounds, step_size=0.5):
    neighbor = [
        max(
            bounds[i][0],
            min(bounds[i][1], solution[i] + random.uniform(-step_size, step_size)),
        )
        for i in range(len(solution))
    ]
    return neighbor


def simulated_annealing(
    func, bounds, max_iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_energy = func(current_solution)
    best_solution = current_solution
    best_energy = current_energy

    for iteration in range(max_iterations):

        new_solution = generate_neighbor(current_solution, bounds)
        new_energy = func(new_solution)
        delta_energy = new_energy - current_energy

        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temp):
            current_solution = new_solution
            current_energy = new_energy

        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy

        temp *= cooling_rate

        if temp < epsilon or abs(delta_energy) < epsilon:
            break

    return best_solution, best_energy
