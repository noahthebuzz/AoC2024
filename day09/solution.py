# Write your solution here
import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc

# Read input from file
path = "day09\input.txt"
data = open(path).read().strip()
print(data + "\n")

result1 = 0
result2 = 0


#######################################################
### PART 1
#######################################################


FILES = deque([])
SPACE = deque([])

position = 0
file_id = 0

FINAL = []

for i, length in enumerate(data):
        if i % 2 == 0:
                for _ in range(int(length)):
                        FILES.append((position, file_id))
                        FINAL.append(file_id)
                        position += 1
                file_id += 1
        else:
                for _ in range(int(length)):
                        SPACE.append(position)
                        FINAL.append(None)
                        position += 1

# print("FILES: " + str(FILES) + "\n")
# print("SPACE: " + str(SPACE) + "\n")
# print("FINAL: " + str(FINAL) + "\n")

size = len(FILES)
FINAL = FINAL[:size]

while FILES[-1][0] > SPACE[0]:
        assert FINAL[SPACE[0]] is None
        FINAL[SPACE[0]] = FILES[-1][1]
        FILES.pop()
        SPACE.popleft()

for i, id in enumerate(FINAL):
        if id is not None:
                result1 += i * id
        else:
                break

print("Part 1: ", str(result1) + "\n")


#######################################################
### PART 2
#######################################################


FILES = deque([])
SPACE = deque([])

position = 0
file_id = 0

FINAL = []

for i, length in enumerate(data):
        if i % 2 == 0:
                FILES.append((position, int(length), file_id))
                for _ in range(int(length)):
                        FINAL.append(file_id)
                        position += 1
                file_id += 1
        else:
                
                if int(length) != 0: 
                        SPACE.append((position, int(length)))
                for _ in range(int(length)):
                        FINAL.append(None)
                        position += 1

# print("FINAL: " + str(FINAL))
# print("FINAL LENGTH: " + str(len(FINAL)) + "\n")
# print("FILES: " + str(FILES) + "\n")
# print("SPACE: " + str(SPACE) + "\n")

for (pos, length, file_id) in reversed(FILES):
        for space_i, (space_pos, space_length) in enumerate(SPACE):
                if space_pos < pos and length <= space_length:
                        for i in range(length):
                                assert FINAL[pos + i] == file_id
                                FINAL[pos + i] = None
                                FINAL[space_pos + i] = file_id
                        if space_length - length == 0:
                                SPACE.popleft()
                        else:
                                SPACE[space_i] = (space_pos + length, space_length - length)
                        break
        

# print("NEW_FINAL: " + str(FINAL))
# print("NEW_SPACE: " + str(SPACE) + "\n")

for i, id in enumerate(FINAL):
        if id is not None:
                result2 += i * id

print("Part 2: ", str(result2) + "\n")