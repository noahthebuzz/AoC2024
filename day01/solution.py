import sys
from collections import Counter

def readInput(path):
        with open(path, "r") as file:
                data = file.readlines()
        
        return data


def parseLists(data):
        first_list = []
        second_list = []

        for line in data:
                (left, right) = map(int, line.split())
                first_list.append(left)
                second_list.append(right)

        return (first_list, second_list)


def calculateDifference(first_list, second_list):
        result = sum(abs(a-b) for (a,b) in zip(first_list, second_list))

        return result


def calculateSimilarityScore(first_list, second_list):
        second_list_counts = Counter(second_list)
        result = sum(num * second_list_counts[num] for num in first_list)

        return result
        

# Run the program
if __name__ == "__main__":
        path = "W:\git\GitHub\Privat\AoC2024\day01\input.txt"
        file = readInput(path)
        
        (first, second) = parseLists(file)

        first.sort()
        second.sort()

        result = calculateDifference(first, second)
        print("Difference: " + str(result))

        score = calculateSimilarityScore(first, second)
        print("Similarity Score: " + str(score))