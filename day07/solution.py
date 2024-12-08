# Write your solution here
import pprint


# Read input from file
path = "day07\input.txt"
with open(path, 'r') as file:
        data = file.readlines()


##########################################
### Part 1
##########################################

result = 0

def is_valid(target, operands):
        if len(operands) == 0:
                return target == 0
        return is_valid(target-operands[-1], operands[:-1]) or target % operands[-1] == 0 and is_valid(target//operands[-1], operands[:-1])

        ###########################
        ### ALTERNATIVE SOLUTION
        ###########################
        # if len(operands) == 1:
        #         return target == operands[0]
        # if is_valid(target, [operands[0] + operands[1]] + operands[2:]):
        #         return True
        # if is_valid(target, [operands[0] * operands[1]] + operands[2:]):
        #         return True
        # return False

for line in data:
        target, operands = line.strip().split(":")
        operands = operands.strip().split(" ")
        target = int(target)
        operands = [int(operand) for operand in operands]

        if is_valid(target, operands):
                result += target


print("Part 1 - Result: " + str(result))


##########################################
### Part 2
##########################################

result2 = 0

def is_valid2(target, operands):
        if len(operands) == 1:
                return target == operands[0]
        if is_valid2(target, [operands[0] + operands[1]] + operands[2:]):
                return True
        if is_valid2(target, [operands[0] * operands[1]] + operands[2:]):
                return True
        if is_valid2(target, [int(str(operands[0]) + str(operands[1]))] + operands[2:]):
                return True
        return False

for line in data:
        target, operands = line.strip().split(":")
        operands = operands.strip().split(" ")
        target = int(target)
        operands = [int(operand) for operand in operands]

        if is_valid2(target, operands):
                result2 += target


print("Part 2 - Result: " + str(result2))