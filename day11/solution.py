# Write your solution here
import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc


# Read input from file
path = "day11\input.txt"
data = list(map(int, open(path).read().strip().split(" ")))
print(data)

result = 0

#If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
#If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
#If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

###############################################
### Part 1
###############################################

new_data = []
blinking = 25 # 25 for Part 1
for _ in range(blinking):
        new_data = []
        for i, x in enumerate(data):
                if x == 0:
                        new_data.append(1)
                elif len(str(x)) % 2 == 0:
                        data_string = str(x)
                        new_data.append(int(data_string[:len(data_string)//2]))
                        new_data.append(int(data_string[len(data_string)//2:]))
                else: 
                        new_data.append(x * 2024)
        data = new_data

result = len(new_data)
print(f"Part 1: {result=}")

###############################################
### Part 2
###############################################

data = list(map(int, open(path).read().strip().split(" ")))

DP_cut = {}
def cut(x):
        if x in DP_cut:
                return DP_cut[x]
        data_string = str(x)
        left = int(data_string[:len(data_string)//2])
        right = int(data_string[len(data_string)//2:])
        ret = (left, right)
        DP_cut[x] = ret
        return ret

DP = {}
def solve(x, blinking):
        if (x, blinking) in DP:
                return DP[(x, blinking)]
        if blinking == 0:
                return 1
        elif x == 0:
                return solve(1, blinking - 1)
        elif len(str(x)) % 2 == 0:
                left, right = cut(x)
                ret = solve(left, blinking - 1) + solve(right, blinking - 1)
        else:
                ret = solve(x * 2024, blinking - 1)
        DP[(x, blinking)] = ret
        if len(DP) % 1000 == 0:
                print(len(DP), x, blinking)
        return ret
        
blinking = 75 
final = 0

for x in data:
        #print(x)
        final += solve(x, blinking)

print(f"Part 2: {final=}")