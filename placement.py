import random
import time
import battleships_complete as bs


def read_file():
    global grid_list
    grid_list = []
    with open("grid.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            grid_list.append(line)
    print_grid()

def write_grid():
    print(grid)
    with open("grid.txt", "a") as f:
        f.write(f"{str(grid)}\n")
    

def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global alphabet
    grid = grid_list[0]

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")

    

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def try_to_place_ship_on_grid(row, col, direction, length):
    """Based on direction will call helper method to try and place a ship on the grid"""
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)

def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = ship_sizes[0]
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
            ship_sizes.pop(0)

def init_vars():
        global grid
        global ship_sizes
        global num_of_ships
        global bullets_start
        global bullets_left
        global game_over
        global num_of_ships_sunk
        global ship_positions
        global index_int
        global index_str
        global grid_size
        global alphabet

        grid = [[]]
        ship_sizes = [6, 4, 4, 3, 3, 3, 2, 2, 2, 2]
        num_of_ships = len(ship_sizes)
        bullets_start = 100
        bullets_left = bullets_start
        game_over = False
        num_of_ships_sunk = 0
        ship_positions = [[]]
        index_int = 0
        index_str = 0
        grid_size = 10
        alphabettotal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphabet = alphabettotal[0: grid_size]

def main():
    init_vars()
    create_grid()
    # print_grid()
    write_grid()

if __name__ == "__main__":
    debug_mode = True
    input = input()
    if input == "1":
        main()
    else: 
        read_file()