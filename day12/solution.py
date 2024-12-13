# Write your solution here
import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc

# Read input from file
path = "day12\input2.txt"
data = open(path).read().strip()
data = data.split("\n")
print(data)

#################################
### Part 1
#################################

result_part1 = 0

# Find unique types of plants
types = set()
for i in range(len(data)):
        for j in range(len(data[i])):
                types.add(data[i][j])

def flood_fill(data, i, j, type, visited):
    stack = [(i, j)]
    area = 0
    perimeter = 0
    sides = set()  # To store unique sides

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        area += 1

        # Check top
        if x == 0 or data[x-1][y] != type:
            perimeter += 1
            sides.add(((x, y), (x-1, y)))
        elif (x-1, y) not in visited:
            stack.append((x-1, y))

        # Check bottom
        if x == len(data) - 1 or data[x+1][y] != type:
            perimeter += 1
            sides.add(((x, y), (x+1, y)))
        elif (x+1, y) not in visited:
            stack.append((x+1, y))

        # Check left
        if y == 0 or data[x][y-1] != type:
            perimeter += 1
            sides.add(((x, y), (x, y-1)))
        elif (x, y-1) not in visited:
            stack.append((x, y-1))

        # Check right
        if y == len(data[x]) - 1 or data[x][y+1] != type:
            perimeter += 1
            sides.add(((x, y), (x, y+1)))
        elif (x, y+1) not in visited:
            stack.append((x, y+1))

    return area, perimeter, len(sides)

t_a_p_s = []
visited = set()
for i in range(len(data)):
    for j in range(len(data[i])):
        if (i, j) not in visited:
            type = data[i][j]
            area, perimeter, sides = flood_fill(data, i, j, type, visited)
            t_a_p_s.append((type, area, perimeter, sides))

# Calculate Part 1 result
for type, area, perimeter, sides in t_a_p_s:
    summand = area * perimeter
    print(f"Type: {type} -> Area: {area} * Perimeter: {perimeter} = Summand: {summand}")
    result_part1 += summand

print(f"Part 1: {result_part1=}")

#################################
### Part 2
#################################
