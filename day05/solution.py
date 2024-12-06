# Write your solution here


# Read input from file
path = "day05\input.txt"
with open(path, 'r') as file:
        data = file.readlines()


##################################################################
### Part 1
##################################################################


rules = {}
updates = [[]]

# Parse input data into rules (dict with int as key, list as value) and updates (list of lists)
for line in data:
        if line.__contains__('|'):
                line = line.removesuffix('\n')
                info = line.split('|')

                if rules.__contains__(int(info[0])):
                        rules[int(info[0])].append(int(info[1]))
                else:
                        rules[int(info[0])] = [int(info[1])]

                #print(rules)

        if line.__contains__(','):
                line = line.removesuffix('\n')
                info = line.split(',')
                updates.append(info)

                #print(updates)

result_updates = updates.copy()
poppers = []

flag = False
for x in range(len(updates)):
        update = updates[x]
        etadpu = update[::-1]
        for i in range(len(update) - 1):
                if not rules.__contains__(int(etadpu[i])):
                        continue

                for j in range(i+1, len(update)):
                        if rules[int(etadpu[i])].__contains__(int(etadpu[j])):
                                print("Current X: " + str(x))
                                poppers.append(x)
                                flag = True
                                break

                if flag:
                        flag = False
                        break

poppers = poppers[::-1]

leftover_updates = []

for popper in poppers:
        leftover_updates.append(result_updates.pop(popper))

result_updates.pop(0)

#print(len(updates))
#print(len(result_updates))

result = 0
for update in result_updates:
        #print(update)
        result += int(update[len(update)//2])

print("Part 1: " + str(result))


##################################################################
### Part 2
##################################################################

#print(leftover_updates)


for update in leftover_updates:
        for i in range(len(update) - 1):
                if not rules.__contains__(int(update[i])):
                        continue

                for j in range(i+1, len(update)):
                        if rules[int(update[i])].__contains__(int(update[j])):
                                update[i], update[j] = update[j], update[i]

result2 = 0

for update in leftover_updates:
        result2 += int(update[len(update)//2])

print("Part 2: " + str(result2))