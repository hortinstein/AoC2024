# Read input and build grid
with open("input", "r") as f:
    data_structure = [line.strip() for line in f]

def print_grid(grid):
    for row in grid:
        print(row)

start_row = 0
start_col = 0
start_dir = 0

direction = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3
}

for row in range(len(data_structure)):
    for col in range(len(data_structure[row])):
        if data_structure[row][col] in direction:
            start_row = row
            start_col = col
            start_dir = direction[data_structure[row][col]],data_structure[row][col]

print("start: row",start_row," col:", start_col, " dir:", start_dir)

directions = [
    (-1, 0),  # Up
    (0, 1),   # Right
    (1, 0),   # Down
    (0, -1),  # Left
]

positions = 0
y, x = start_row, start_col
d = start_dir[0]
dx = directions[d][1]
dy = directions[d][0]

def print_grid(grid, x, y):
    for row in range(len(grid)):
        if row == y:
            print(grid[row][:x] + "X" + grid[row][x+1:])
        else:
            print(grid[row])
    print("\n")

positions = set()

while True:
    if x < 0 or x >= len(data_structure)-1 or y < 0 or y >= len(data_structure[0])-1:
        break
    dx = directions[d][1]
    dy = directions[d][0]
    #move directioon
    x += dx
    y += dy
    positions.add((x, y))
    try:
        if data_structure[y+dy][x+dx] == "#":
            print_grid(data_structure, x, y)
            d = (d + 1) % 4
    except:
        break   
print("part1",len(positions))