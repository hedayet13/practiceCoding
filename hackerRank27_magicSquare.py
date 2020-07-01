possibilities = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

s = []
for i in range(3):
    s.append([int(x) for x in input().split(' ')])

min_cost = None
for p in possibilities:
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(p[i][j] - s[i][j])
    if min_cost is None or cost < min_cost:
        min_cost = cost
print(min_cost)

import itertools

s = []
for i in range(3):
    s.extend(list(map(int, input().split(" "))))

min_cost = 1000
best = None


def is_magic(s):
    for i in range(3):
        if sum(s[i * 3:i * 3 + 3]) != 15:
            return False
        if sum(s[i::3]) != 15:
            return False
    if s[0] + s[4] + s[8] != 15:
        return False
    if s[2] + s[4] + s[6] != 15:
        return False
    return True


best = None
for p in itertools.permutations(range(1, 10)):
    cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
    if cost < min_cost and is_magic(p):
        min_cost = cost
        best = p

print(min_cost)