import re

# Read input from file
path = "W:\git\GitHub\Privat\AoC2024\day03\input.txt"
with open(path, 'r') as file:
    data = file.readlines()


#########################################
### PART 1
#########################################

muls = []

# Appends all occurings of the word "mul(number, number)" to the list
for line in data:
        muls += re.findall(r'mul\(\d+,\d+\)', line)

result = 0

# Gets the two numbers from the string, multiplies them and adds them to the result
for mul in muls:
        nums = []
        nums = re.findall(r'\d+', mul)
        result += int(nums[0]) * int(nums[1])

print("Part 1 - Result: " + str(result))


#########################################
### PART 2
#########################################

muls = []

# Appends all occurings of "mul(number, number)", "do()" and "don't()" to the list in the order they appear
for line in data:
        #muls += re.findall(r'mul\(\d+,\d+\)', line)
        muls += re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)

result = 0
do = True

# Ignores everything after a "don't()" until a "do()" appears
for mul in muls:
        if "don't" in mul:
                do = False
                continue
        elif "do" in mul:
                do = True
                continue
        
        if do:
                nums = []
                nums = re.findall(r'\d+', mul)
                result += int(nums[0]) * int(nums[1])
        else:
                continue

print("Part 2 - Result: " + str(result))