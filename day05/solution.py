# Write your solution here


# Read input from file
path = "W:\git\GitHub\Privat\AoC2024\day05\input.txt"
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

for update in updates:
        etadpu = update[::-1]
        for i in range(len(update)):
                if not rules.__contains__(int(etadpu[i])):
                        continue

                for j in range(i+1, len(update)):
                        None