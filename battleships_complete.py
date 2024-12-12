import random
import time

"""
    -------BATTLESHIPS-------
    Pre-reqs: Loops, Strings, Arrays, 2D Arrays, Global Variables, Methods
    How it will work:
    1. A 10x10 grid will have 8 ships of variable length randomly placed about
    2. You will have 50 bullets to take down the ships that are placed down
    3. You can choose a row and column such as A3 to indicate where to shoot
    4. For every shot that hits or misses it will show up in the grid
    5. A ship cannot be placed diagonally, so if a shot hits the rest of
        the ship is in one of 4 directions, left, right, up, and down
    6. If all ships are unearthed before using up all bullets, you win
        else, you lose

    Legend:
    1. "." = water or empty space
    2. "O" = part of ship
        only if debugMode is on, else it will show as "."
    3. "X" = part of ship that was hit with bullet
    4. "#" = water that was shot with bullet, a miss because it hit no ship

    this code was moddified by Adrian Bleeker to fix the issuses with the original code and to use for his School Project
"""
# Modes mode 
debug_mode = True
test_mode = True

# Global variable for grid size

# Global variable for alphabet
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Global variable for grid
# grid = [[]]
# Global variable for number of ships to place
# ship_sizes = [6, 4, 4, 3, 3, 3, 2, 2, 2, 2]
# num_of_ships = len(ship_sizes)
# Global variable for bullets left
# bullets_start = 100
# bullets_left = bullets_start
# Global variable for game over
# game_over = False
# Global variable for number of ships sunk
# num_of_ships_sunk = 0
# Global variable for ship positions
# ship_positions = [[]]
def test1():
    placement_y = random.choice(alphabet)
    placement_x = random.randint(0, 9)
    placement = f"{placement_y}{placement_x}"

    return placement
def test2():
    """
    will test all cases line for line
    """
    global index_str
    global index_int
    placement_y = alphabet[index_str]
    placement_x = index_int
    index_int += 1
    if index_str == 10: 
        index_str = 0
    if index_int == 10:
        index_int = 0
        index_str += 1
    return f"{placement_y}{placement_x}"
        


def test_input():
    """Will return test input for testing purposes as string of letter in alphabet and number"""
    # return test1()
    return test2()

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


def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

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


def accept_valid_bullet_placement():
    """Will get valid row and column to place bullet shot"""
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:

        try:
            # use the terminal as input or the test_input function for testing
            if test_mode:
                placement = test_input()
            elif not test_mode:
                placement = input("Enter row (A-J) and column (0-9) such as A3: ")
            placement = placement.upper()
            if len(placement) <= 0 or len(placement) > 2:
                print("Error: Please enter only one row and column such as A3")
                continue
            row = placement[0]
            col = placement[1]
            if not row.isalpha() or not col.isnumeric():
                print("Error: Please enter letter (A-J) for row and (0-9) for column")
                continue
            row = alphabet.find(row)
            if not (-1 < row < grid_size):
                print("Error: Please enter letter (A-J) for row and (0-9) for column")
                continue
            col = int(col)
            if not (-1 < col < grid_size):
                print("Error: Please enter letter (A-J) for row and (0-9) for column")
                continue
        except IndexError:
            print("Error: Please enter letter (A-J) for row and (0-9) for column")
        if (grid[row][col] == "#" or grid[row][col] == "X") and not test_mode: # type: ignore
            print("You have already shot a bullet here, pick somewhere else")
            continue
        if grid[row][col] == "." or grid[row][col] == "O": # type: ignore
            is_valid_placement = True


    return row, col


def check_for_ship_sunk(row, col):
    """If all parts of a shit have been shot it is sunk and we later increment ships sunk"""
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if (start_row <= row < end_row) and (start_col <= col < end_col):
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    print("A ship was completely sunk!")
    return True


def shoot_bullet():
    """Updates grid and ships based on where the bullet was shot"""
    global grid
    global num_of_ships_sunk
    global bullets_left

    row, col = accept_valid_bullet_placement()
    print("")
    print("----------------------------")

    if grid[row][col] == ".": # type: ignore
        print("You missed, no ship was shot")
        grid[row][col] = "#" # type: ignore
    elif grid[row][col] == "O": # type: ignore
        print("You hit!", end=" ")
        grid[row][col] = "X" # type: ignore
        if check_for_ship_sunk(row, col):
            num_of_ships_sunk += 1
        else:
            print("A ship was shot")

    bullets_left -= 1


def check_for_game_over():
    """If all ships have been sunk or we run out of bullets its game over"""
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print("Congrats you won!")
        game_over = True
    elif bullets_left <= 0:
        print("Sorry, you lost! You ran out of bullets, try again next time!")
        game_over = True


def main():
    """Main entry point of application that runs the game loop"""
    global game_over

    print("-----Welcome to Battleships-----")
    print(f"You have {bullets_left} bullets to take down {num_of_ships} ships, may the battle begin!")

    create_grid()

    while game_over is False:
        # print_grid()
        # print("Number of ships remaining: " + str(num_of_ships - num_of_ships_sunk))
        # print("Number of bullets left: " + str(bullets_left))
        shoot_bullet()
        # print("----------------------------")
        # print("")
        check_for_game_over()
        # time.sleep(1)
    if test_mode:
        with open('random_test.txt', 'a') as f:
            f.write(f"{bullets_start-bullets_left}\n")

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

def mainloop():
    for i in range(10): 
        init_vars()
        main()
if __name__ == '__main__':
    """Will only be called when program is run from terminal or an IDE like PyCharms"""
    # main()
    mainloop()