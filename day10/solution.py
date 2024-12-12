# Write your solution here
import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc


# Read input from file
path = "day10\input.txt"
data = open(path).read().strip()
print(data)


###############################################
### Part 1
###############################################

map = [[]]
for line in data.split("\n"):
        map.append([int(x) for x in line])
map = map[1:]
#print(map)

def find_9(map, number, x, y, trailhead):
        if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]):
                return
        if map[x][y] != (number):
                return
        if number == 9:
                print(f"[DEBUG]: {number=}, {x=}, {y=}")
                print(f"[DEBUG]: added 1 to score")
                trailhead.add((x, y))
                return 
        find_9(map, map[x][y] + 1, x + 1, y, trailhead)
        find_9(map, map[x][y] + 1, x - 1, y, trailhead)
        find_9(map, map[x][y] + 1, x, y + 1, trailhead)
        find_9(map, map[x][y] + 1, x, y - 1, trailhead)
        return len(trailhead)
       

width = len(map)
height = len(map[0])
score = 0
for row in range(width):
        for col in range(height):
                if map[row][col] == 0:
                        sr, sc = row, col
                        trailhead = set()
                        new_score = find_9(map, 0, sr, sc, trailhead)
                        score += new_score
                        print(f"[DEBUG]: {new_score=}, {row=}, {col=}")

print("Part 1:", score)


###############################################
### Part 2
###############################################

map = [[]]
for line in data.split("\n"):
        map.append([int(x) for x in line])
map = map[1:]
#print(map)

def find_9(map, number, x, y):
        if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]):
                return 0
        if map[x][y] != (number):
                return 0
        if number == 9:
                #print(f"[DEBUG]: {number=}, {x=}, {y=}")
                #print(f"[DEBUG]: added 1 to score")
                return 1
        return find_9(map, map[x][y] + 1, x, y - 1) + find_9(map, map[x][y] + 1, x, y + 1) + find_9(map, map[x][y] + 1, x - 1, y) + find_9(map, map[x][y] + 1, x + 1, y)
       

width = len(map)
height = len(map[0])
score = 0
for row in range(width):
        for col in range(height):
                if map[row][col] == 0:
                        sr, sc = row, col
                        new_score = find_9(map, 0, sr, sc)
                        score += new_score
                        print(f"[DEBUG]: {new_score=}, {row=}, {col=}")

print("Part 2:", score)