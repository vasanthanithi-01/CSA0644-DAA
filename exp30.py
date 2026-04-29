from itertools import combinations

def knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_items = []

    for r in range(n + 1):
        for comb in combinations(range(n), r):
            total_weight = 0
            total_value = 0

            for i in comb:
                total_weight += weights[i]
                total_value += values[i]

            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_items = list(comb)

    return best_items, max_value

weights = [2, 3, 1]
values = [4, 5, 3]
capacity = 4

print(knapsack(weights, values, capacity))