# Write your solution here
import pprint


# Read input from file
path = "day06\input.txt"
with open(path, 'r') as file:
        data = file.readlines()


#######################################
### NEW SOLUTION
#######################################

res1 = 0
res2 = 0

GAME = [[]]
for line in data:
        GAME.append(list(line.strip()))

GAME.pop(0)

print(GAME)

ROW = len(GAME)
COL = len(GAME[0])

for r in range(ROW):
        for c in range(COL):
                if GAME[r][c] == '^':
                        start_row, start_col = r, c

for o_x in range(ROW):
        for o_y in range(COL):
                print("[DEBUG]: X: " + str(o_x) + " - Y: " + str(o_y))

                x,y = start_row, start_col
                d = 0 # DIRECTION 0 = up, 1 = right, 2 = down, 3 = left
                SEEN_DIR = set()
                SEEN = set()

                while True:
                        if (x,y,d) in SEEN_DIR:
                                res2 += 1
                                break

                        SEEN_DIR.add((x,y,d))
                        SEEN.add((x,y))

                        dx, dy = [(-1,0),(0,1),(1,0),(0,-1)][d]
                        new_x = x + dx
                        new_y = y + dy

                        if not (0 <= new_x < ROW and 0 <= new_y < COL):
                                if GAME[o_x][o_y] == '#':
                                        res1 = len(SEEN)
                                break

                        if GAME[new_x][new_y] == '#' or new_x == o_x and new_y == o_y:
                                d = (d + 1) % 4
                        else:
                                x = new_x
                                y = new_y

print("Part 1: " + str(res1))
print("Part 2: " + str(res2))



#######################################
### OLD SOLUTION
#######################################


#############################
### Part 1
#############################
        

# def turn_data_into_map(data):
#         return [list(line.strip()) for line in data]


# def get_player_position(map):
#         for y, row in enumerate(map):
#                 for x, cell in enumerate(row):
#                         if cell in ['^', '>', 'v', '<']:
#                                 return (x, y)
#         return None


# def turn_player(player):
#         directions = {
#                 '^': '>',
#                 '>': 'v',
#                 'v': '<',
#                 '<': '^'
#         }
#         return directions.get(player, '^')
        

# def determine_new_player_position(position, player):
#         x, y = position
#         moves = {
#                 '^': (0, -1),
#                 '>': (1, 0),
#                 'v': (0, 1),
#                 '<': (-1, 0)
#         }
#         dx, dy = moves.get(player, (0, 0))
#         return (x + dx, y + dy)


# def is_player_in_front_of_wall(map, position, player):
#         x, y = position
#         x1, y1 = determine_new_player_position(position, player)
#         if 0 <= x1 < len(map[0]) and 0 <= y1 < len(map):
#                 return map[y1][x1] == '#' or map[y1][x1] == 'O'
#         return False


# def change_map(game_map, old_position, new_position, player):
#         x, y = old_position
#         x1, y1 = new_position
#         if 0 <= x1 < len(game_map[0]) and 0 <= y1 < len(game_map):
#                 game_map[y][x] = 'X'
#                 game_map[y1][x1] = player
#         else:
#                 game_map[y][x] = 'X'
#         return game_map


# def is_game_over(map):
#         return get_player_position(map) is None


# def gameloop(map):
#         player = '^'
#         position = get_player_position(map)
#         while not is_game_over(map):
#                 if is_player_in_front_of_wall(map, position, player):
#                         player = turn_player(player)
#                         map = change_map(map, position, position, player)
#                 else:
#                         new_position = determine_new_player_position(position, player)
#                         map = change_map(map, position, new_position, player)
#                         position = new_position
#         return map


# game_map = turn_data_into_map(data)
# final_map = gameloop(game_map)
# print(final_map)
# print("Part 1: " + str(sum([row.count('X') for row in final_map])))


#############################
### Part 2
#############################
### NOT WORKING

# new_game_map = turn_data_into_map(data) 

# def find_number_of_loops(map):
#     player = '^'
#     original_position = get_player_position(map)
#     loops = 0

#     def is_guard_stuck(map, position, player):
#         visited_walls = set()
#         steps = 0  # Debug: Track the number of steps
#         while not is_game_over(map):
#                 if position in visited_walls:
#                         print(f"Guard stuck after {steps} steps at position {position}")  # Debug
#                         visited_walls.clear()
#                         return True
#                 if is_player_in_front_of_wall(map, position, player):
#                         visited_walls.add(position)
#                         player = turn_player(player)
#                         map = change_map(map, position, position, player)
#                 else:
#                         new_position = determine_new_player_position(position, player)
#                         map = change_map(map, position, new_position, player)
#                         position = new_position
#                 steps += 1  # Debug
#         return False

#     for y, row in enumerate(map):
#         for x, cell in enumerate(row):
#             if cell == '.':
#                 print(f"Testing position ({x}, {y})")  # Debug
#                 map[y][x] = 'O'
#                 if is_guard_stuck(map, original_position, player):
#                     loops += 1
#                     print(loops)
#                 map[y][x] = '.'  # Restore the map after testing

#     return loops

# print("Part 2: " + str(find_number_of_loops(new_game_map)))