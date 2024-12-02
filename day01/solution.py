import sys
from collections import Counter

# Read input from file
path = "W:\git\GitHub\Privat\AoC2024\day01\input.txt"
with open(path, 'r') as file:
    data = file.readlines()

# Parse the input into two lists
left_list = []
right_list = []
for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Part 1: Calculate total distance between the lists
# Sort both lists
sorted_left = sorted(left_list)
sorted_right = sorted(right_list)

# Calculate the total distance
total_distance = sum(abs(a - b) for a, b in zip(sorted_left, sorted_right))
print("Part 1: Total Distance:", total_distance)

# Part 2: Calculate similarity score
# Count occurrences of each number in the right list
right_counts = Counter(right_list)

# Calculate the similarity score
similarity_score = sum(num * right_counts[num] for num in left_list)
print("Part 2: Similarity Score:", similarity_score)