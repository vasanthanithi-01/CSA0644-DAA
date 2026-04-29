from itertools import permutations

def assignment_problem(cost):
    n = len(cost)
    min_cost = float('inf')
    best = []

    for perm in permutations(range(n)):
        total = 0

        for i in range(n):
            total += cost[i][perm[i]]

        if total < min_cost:
            min_cost = total
            best = perm

    return best, min_cost

cost = [
    [3, 10, 7],
    [8, 5, 12],
    [4, 6, 9]
]

print(assignment_problem(cost))