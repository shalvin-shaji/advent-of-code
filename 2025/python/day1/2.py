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
        direction, value = movement

        # Counting the times we might have crossed
        count += value // 100
        # We just need to move only value % 100 remaining clicks
        movement = (direction, value % 100)
        new_position = move(current, movement)

        if new_position == 0:
            # We landed in zero, increment the count
            count += 1
        elif direction == "R" and new_position < current and current != 0:
            # Even though we moved to right we ended up in a position that is less than previos position
            # We are handing zero seperately since moveing from to any position should not be counted
            count += 1
        elif direction == "L" and new_position > current and current != 0:
            # We ended up in a position greater that previous position on moving left,
            # we should have crossed zero
            count += 1
        current = new_position

    print(count)


solve()
