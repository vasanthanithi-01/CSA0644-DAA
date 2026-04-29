from itertools import permutations
import math

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def tsp(cities):
    start = cities[0]
    min_dist = float('inf')
    best_path = []

    for path in permutations(cities[1:]):
        total = 0
        route = [start] + list(path) + [start]

        for i in range(len(route) - 1):
            total += distance(route[i], route[i + 1])

        if total < min_dist:
            min_dist = total
            best_path = route

    return min_dist, best_path

cities = [(1, 2), (4, 5), (7, 1), (3, 6)]
print(tsp(cities))