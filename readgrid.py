from ast import literal_eval as ast

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")

def read_file_to_list(filename):
    # Create an empty list to store the lines
    data = []
    
    # Open the file in read mode
    with open("tests/"+filename, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip any leading/trailing whitespace and convert the string to a list using ast.literal_eval
            line_list = ast(line.strip())
            data.append(line_list)
    
    return data

# Example usage
filename = 'grid.txt'  # Replace with your file's path
result = read_file_to_list(filename)

# Print the result
for line in result:
    # print(line)
    for i in range(10):
        for j in range(10):
            if line[i][j] == "O":
                grid[i][j] += 1
print_grid()
print(len(result))
    


# dict = {
#     "A1": "",
#     "A2": "",
#     "A3": "",
#     "A4": "",
#     "A5": "",
#     "A6": "",
#     "A7": "",
#     "A8": "",
#     "A9": "",
#     "B1": "",
#     "B2": "",
#     "B3": "",
#     "B4": "",
#     "B5": "",
#     "B6": "",
#     "B7": "",
#     "B8": "",
#     "B9": "",
#     "C1": "",
#     "C2": "",
#     "C3": "",
#     "C4": "",
#     "C5": "",
#     "C6": "",
#     "C7": "",
#     "C8": "",
#     "C9": "",
#     "D1": "",
#     "D2": "",
#     "D3": "",
#     "D4": "",
#     "D5": "",
#     "D6": "",
#     "D7": "",
#     "D8": "",
#     "D9": "",
#     "E1": "",
#     "E2": "",
#     "E3": "",
#     "E4": "",
#     "E5": "",
#     "E6": "",
#     "E7": "",
#     "E8": "",
#     "E9": "",
#     "F1": "",
#     "F2": "",
#     "F3": "",
#     "F4": "",
#     "F5": "",
#     "F6": "",
#     "F7": "",
#     "F8": "",
#     "F9": "",
#     "G1": "",
#     "G2": "",
#     "G3": "",
#     "G4": "",
#     "G5": "",
#     "G6": "",
#     "G7": "",
#     "G8": "",
#     "G9": "",
#     "H1": "",
#     "H2": "",
#     "H3": "",
#     "H4": "",
#     "H5": "",
#     "H6": "",
#     "H7": "",
#     "H8": "",
#     "H9": "",
#     "I1": "",
#     "I2": "",
#     "I3": "",
#     "I4": "",
#     "I5": "",
#     "I6": "",
#     "I7": "",
#     "I8": "",
#     "I9": "",
#     "J1": "",
#     "J2": "",
#     "J3": "",
#     "J4": "",
#     "J5": "",
#     "J6": "",
#     "J7": "",
#     "J8": "",
#     "J9": ""
# }