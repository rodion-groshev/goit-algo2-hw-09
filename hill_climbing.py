import numpy as np
import random


def get_neighbors(current, step_size=0.1):
    return [
        [current[i] + (step_size if j == i else 0) for i in range(len(current))]
        for j in range(len(current))
    ] + [
        [current[i] - (step_size if j == i else 0) for i in range(len(current))]
        for j in range(len(current))
    ]


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1):
    current_solution = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        neighbors = get_neighbors(current_solution, step_size)

        neighbors = [
            [max(bounds[i][0], min(bounds[i][1], n[i])) for i in range(len(bounds))]
            for n in neighbors
        ]

        next_solution = None
        next_value = np.inf

        for neighbor in neighbors:
            value = func(neighbor)

            if value < next_value:
                next_solution = neighbor
                next_value = value

        if abs(current_value - next_value) < epsilon:
            break

        current_solution, current_value = next_solution, next_value

    return current_solution, current_value
