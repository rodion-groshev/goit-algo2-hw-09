import random


def get_random_neighbor(current, bounds, step_size=0.5):
    x, y = current
    new_x = x + random.uniform(-step_size, step_size)
    new_y = y + random.uniform(-step_size, step_size)

    new_x = max(bounds[0][0], min(bounds[0][1], new_x))
    new_y = max(bounds[1][0], min(bounds[1][1], new_y))

    return new_x, new_y


def random_local_search(func, bounds, max_iterations=1000, epsilon=1e-6, step_size=0.5):
    current_point = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current_point)

    for iteration in range(max_iterations):
        new_point = get_random_neighbor(current_point, bounds, step_size)
        new_value = func(new_point)

        if new_value < current_value:
            current_point, current_value = new_point, new_value

    return current_point, current_value
