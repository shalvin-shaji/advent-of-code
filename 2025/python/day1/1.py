import sys

filename = sys.argv[1]

inputs = [(line[0], int(line[1:])) for line in open(filename, "r").readlines()]


initial = 50


def move(current, movement):
    direction, value = movement
    if direction == "R":
        current += value
    elif direction == "L":
        current -= value
    return current % 100


def solve():
    current = initial
    count = 0
    for movement in inputs:
        current = move(current, movement)
        if current == 0:
            count += 1
    print(count)


solve()
