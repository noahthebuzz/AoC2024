

# Read input from file
path = "W:\git\GitHub\Privat\AoC2024\day04\input.txt"
with open(path, 'r') as file:
    data = file.readlines()


#########################################
### PART 1
#########################################


field = [['' for col in range(len(data[0]))] for row in range(len(data))]

for i in range(len(data)):
        for j in range(len(data[i])):
                field[i][j] = data[i][j]



# find all ocrruings of the word "XMAS" in the field, either horizontal, vertical, diagonal or written backwards in any of these directions
# return the total number of occurings


# data[x][y] -> y is horizontal, x is vertical
def find_all_horizontal_occurings(field):
        occurings = 0

        word = ""
        drow = ""
        for i in range(len(field)):
                for j in range(len(field[i]) - 3):
                        word = field[i][j] + field[i][j+1] + field[i][j+2] + field[i][j+3]
                        drow = word[::-1]

                        if word == "XMAS" or drow == "XMAS":
                                occurings += 1

        return occurings


# data[x][y] -> y is horizontal, x is vertical
def find_all_vertical_occurings(field):
        occurings = 0

        word = ""
        drow = ""

        for i in range(len(field) - 3):
                for j in range(len(field[i])):
                        word = field[i][j] + field[i+1][j] + field[i+2][j] + field[i+3][j]
                        drow = word[::-1]

                        if word == "XMAS" or drow == "XMAS":
                                occurings += 1

        return occurings


# data[x][y] -> y is horizontal, x is vertical
def find_all_diagonal_occurings(field):
        occurings = 0

        word = ""
        drow = ""

        for i in range(len(field) - 3):
                for j in range(len(field[i]) - 3):
                        word = field[i][j] + field[i+1][j+1] + field[i+2][j+2] + field[i+3][j+3]
                        drow = word[::-1]

                        if word == "XMAS" or drow == "XMAS":
                                occurings += 1

        for i in range(len(field) - 3):
                for j in range(len(field[i]) - 3):
                        word = field[i][j+3] + field[i+1][j+2] + field[i+2][j+1] + field[i+3][j]
                        drow = word[::-1]

                        if word == "XMAS" or drow == "XMAS":
                                occurings += 1

        return occurings

total_occurings = find_all_horizontal_occurings(field) + find_all_vertical_occurings(field) + find_all_diagonal_occurings(field)
print("Part 1 - Total occurings: ", total_occurings)
        

#########################################
### PART 2
#########################################

def find_all_x_mas(field):
        occurings = 0

        word = ""
        drow = ""
        for i in range(len(field) - 2):
                for j in range(len(field[i]) - 2):
                        word = field[i][j] + field[i+1][j+1] + field[i+2][j+2]
                        drow = word[::-1]
                        word2 = field[i][j+2] + field[i+1][j+1] + field[i+2][j]
                        drow2 = word2[::-1]

                        if word == "MAS" or drow == "MAS":
                                if word2 == "MAS" or drow2 == "MAS":
                                        occurings += 1

        return occurings

total_occurings = find_all_x_mas(field)
print("Part 2 - Total occurings: ", total_occurings)