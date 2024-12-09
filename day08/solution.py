# Write your solution here


# Read input from file
path = "day08\input.txt"
with open(path, 'r') as file:
        data = file.readlines()

result1 = 0
result2 = 0

#######################################
### TASK 1
#######################################

frequency = set()
antinodes = set()

for line in data:
        line = line.strip()
        for dot in line:
                if not dot == '.':
                        frequency.add(dot)

rows = len(data)
cols = len(data[0].strip())

occurrences = 0

for fr in frequency:
        locations = set()
        occurrences = 0
        for x in range(rows):
                for y in range(cols):
                        if data[x][y] == fr:
                                locations.add((x,y))
                                occurrences += 1

        locations = list(locations)
        print("[DEBUG]: checking '" + fr + "' - (occurrences: " + str(occurrences) + ")")
        counter = 0
        # Find antinodes
        for i in range(len(locations) - 1):
                for j in range(i+1 ,len(locations)):
                        x1, y1 = locations[i]
                        x2, y2 = locations[j]
                        print("[DEBUG]: X1: " + str(x1) + " - Y1: " + str(y1))
                        print("[DEBUG]: X2: " + str(x2) + " - Y2: " + str(y2))

                        # Abstände
                        x_dist = abs(x1 - x2)
                        y_dist = abs(y1 - y2)

                        # Mittlere location
                        x_mid = (x1 + x2) / 2
                        y_mid = (y1 + y2) / 2

                        # Calculate new positions based on the relative positions of (x1, y1) and (x2, y2)
                        if x1 >= x2:
                            x_factor1, x_factor2 = 1.5, -1.5
                        else:
                            x_factor1, x_factor2 = -1.5, 1.5

                        if y1 >= y2:
                            y_factor1, y_factor2 = 1.5, -1.5
                        else:
                            y_factor1, y_factor2 = -1.5, 1.5

                        new_x1 = x_mid + x_factor1 * x_dist
                        new_y1 = y_mid + y_factor1 * y_dist
                        new_x2 = x_mid + x_factor2 * x_dist
                        new_y2 = y_mid + y_factor2 * y_dist

                        if new_x1 in range(rows) and new_y1 in range(cols):
                                counter += 1
                                print("[DEBUG]: added X:" + str(new_x1) + " - Y:" + str(new_y1) + " - Counter: " + str(counter))
                                antinodes.add((new_x1, new_y1))
                        if new_x2 in range(rows) and new_y2 in range(cols):
                                counter += 1
                                print("[DEBUG]: added X:" + str(new_x2) + " - Y:" + str(new_y2) + " - Counter: " + str(counter))
                                antinodes.add((new_x2, new_y2))
        print("[DEBUG]: '" + fr + "' has this many antinodes: " + str(counter))

# antinodes = list(antinodes)
# antinodes.sort()
# print(antinodes)
result1 = len(antinodes)
print("Task 1: " + str(result1))


#######################################
### TASK 2
#######################################

frequency = set()
antinodes = set()

for line in data:
        line = line.strip()
        for dot in line:
                if not dot == '.':
                        frequency.add(dot)

rows = len(data)
cols = len(data[0].strip())

occurrences = 0

for fr in frequency:
        locations = set()
        occurrences = 0
        for x in range(rows):
                for y in range(cols):
                        if data[x][y] == fr:
                                locations.add((x,y))
                                occurrences += 1

        locations = list(locations)
        print("[DEBUG]: checking '" + fr + "' - (occurrences: " + str(occurrences) + ")")
        counter = 0
        # Find antinodes
        for i in range(len(locations) - 1):
                for j in range(i+1 ,len(locations)):
                        x1, y1 = locations[i]
                        x2, y2 = locations[j]
                        print("[DEBUG]: X1: " + str(x1) + " - Y1: " + str(y1))
                        print("[DEBUG]: X2: " + str(x2) + " - Y2: " + str(y2))

                        # Abstände
                        x_dist = abs(x1 - x2)
                        y_dist = abs(y1 - y2)

                        # Mittlere location
                        x_mid = (x1 + x2) / 2
                        y_mid = (y1 + y2) / 2

                        for k in range(0, 100):
                                # Calculate new positions based on the relative positions of (x1, y1) and (x2, y2)
                                if x1 >= x2:
                                        x_factor1, x_factor2 = 0.5 + k, -0.5 - k
                                else:
                                        x_factor1, x_factor2 = -0.5 - k, 0.5 + k

                                if y1 >= y2:
                                        y_factor1, y_factor2 = 0.5 + k, -0.5 - k
                                else:
                                        y_factor1, y_factor2 = -0.5 - k, 0.5 + k

                                new_x1 = x_mid + x_factor1 * x_dist
                                new_y1 = y_mid + y_factor1 * y_dist
                                new_x2 = x_mid + x_factor2 * x_dist
                                new_y2 = y_mid + y_factor2 * y_dist

                                if new_x1 in range(rows) and new_y1 in range(cols):
                                        counter += 1
                                        print("[DEBUG]: added X:" + str(new_x1) + " - Y:" + str(new_y1) + " - Counter: " + str(counter))
                                        antinodes.add((new_x1, new_y1))
                                if new_x2 in range(rows) and new_y2 in range(cols):
                                        counter += 1
                                        print("[DEBUG]: added X:" + str(new_x2) + " - Y:" + str(new_y2) + " - Counter: " + str(counter))
                                        antinodes.add((new_x2, new_y2))
        print("[DEBUG]: '" + fr + "' has this many antinodes: " + str(counter))

# antinodes = list(antinodes)
# antinodes.sort()
# print(antinodes)
result2 = len(antinodes)
print("Task 2: " + str(result2))