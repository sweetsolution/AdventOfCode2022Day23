##############################
# Advent of Code 2022
# Day 23, part a and b of puzzle
# Matthias, 2022-12-23
##############################
from operator import add

def print_grove(grove):
    max_x = 0
    max_y = 0
    text = ""
    for tile in grove:
        max_x = max(max_x, tile[0])
        max_y = max(max_y, tile[1])
    
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            tile = grove.get((x, y), ".")
            text+=tile
        text += ('\n')
    print(f"\n{text}")


def is_area_free(grove, elf_coordinate, dirs):
    for value in dirs:
        tile = grove.get((elf_coordinate[0] + value[0], elf_coordinate[1] + value[1]), '.')
        if tile == '#':
            return False
    return True


def get_elves(groove):
    elves=[]
    for coord, element in grove.items():
        if element == "#":
            elves.append((coord, element))
    return elves


def move(grove):
    round = 0
    dirs = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0), "NE": (1, -1), "NW": (-1, -1), "SW": (-1, 1), "SE": (1, 1)}
    moves = [("N", ["N", "NE", "NW"]), ("S", ["S", "SE", "SW"]), ("W", ["W", "NW", "SW"]), ("E", ["E", "NE", "SE"])]

    move = moves[0]
    #for _ in range(0, 10):
    while(True):    
        round+= 1
        print(f"-- round -- {round}")
        elves=get_elves(grove)
        move_list = {}

        for elf in elves:

            if is_area_free(grove, elf[0], dirs.values()) == True:
                continue

            # check movement in 4 directions
            for mov_cnt in range(0, 4):
                move_pointer_current = mov_cnt
                areas_to_check = [moves[move_pointer_current][1][0], moves[move_pointer_current][1][1], moves[move_pointer_current][1][2]]
                areas_to_check = [dirs[x] for x in areas_to_check]
                if is_area_free(grove, elf[0], areas_to_check):
                    target_coordinate = tuple(list( map(add, elf[0], dirs[moves[move_pointer_current][0]]) ))
                    if target_coordinate in move_list:
                        del move_list[target_coordinate]
                    else:
                        move_list[target_coordinate] = elf[0]
                    break
            
        if len(move_list) == 0:
            return
        for target, elf in move_list.items():
            grove[target] = "#"
            grove[elf] = "."

        print_grove(grove)
        movement = moves.pop(0)
        moves.insert(len(moves), movement)

def parse():
    with open("input.txt") as f:
        contents = f.read()

    grove={}
    lines = contents.split("\n")
    for index_y, line in enumerate(lines):
        for index_x, tile in enumerate(line):
            grove[(index_x, index_y)] = tile
    return grove


grove = parse()
move(grove)

xmax = 0
xmin = 100000000000
ymax = 0
ymin = 100000000000
for coord, item in grove.items():
    if item == '#':
        xmax = max(xmax, coord[0])
        xmin = min(xmin, coord[0])
        ymax = max(ymax, coord[1])
        ymin = min(ymin, coord[1])

free = 0
for y in range(ymin, ymax+1):
    for x in range(xmin, xmax+1):
        if grove.get((x,y), '.') == '.':
            free +=1

print(f"free tiles = {free}")