# Function to search in all 8 directions
def search_word(grid, word, row, col, direction, rows, cols):
    # Direction vectors for 8 possible directions
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Up-Left Diagonal
        (-1, 1),  # Up-Right Diagonal
        (1, -1),  # Down-Left Diagonal
        (1, 1)    # Down-Right Diagonal
    ]

    # Extract direction
    dx, dy = directions[direction]

    # Check each character
    for i in range(len(word)):
        x, y = row + i * dx, col + i * dy
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != word[i]:
            return False
    return True

# Search XMAS
def x_mas(grid,row,column) :
    #check to see if it's an a
    try:
        if grid[row][column] == "A":
            print(grid[row-1][column-1]) 
            if (grid[row-1][column-1] == "M" and grid[row+1][column+1] == "S") and (grid[row-1][column+1] == "M" and grid[row+1][column-1] == "S"):
                return True
            if (grid[row-1][column-1] == "S" and grid[row+1][column+1] == "M") and (grid[row-1][column+1] == "S" and grid[row+1][column-1] == "M"):
                return True
            if (grid[row-1][column-1] == "M" and grid[row+1][column+1] == "S") and (grid[row-1][column+1] == "S" and grid[row+1][column-1] == "M"):
                return True
            if (grid[row-1][column-1] == "S" and grid[row+1][column+1] == "M") and (grid[row-1][column+1] == "M" and grid[row+1][column-1] == "S"):
                return True
    except:
        return False

# Main function to find a word in the grid
def find_word(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0
    count_2 = 0
    for row in range(rows):
        for col in range(cols):
            if x_mas(grid,row,col):
                count_2 += 1
                continue
            # Check in all 8 directions
            for direction in range(8):
                if search_word(grid, word, row, col, direction, rows, cols):
                    count += 1
    
    print("Count 2",count_2)
    return count

# Read input and build grid
with open("input", "r") as f:
    data_structure = [line.strip() for line in f]

# Example usage
word_to_search = "XMAS"  # Replace with the word you want to find

print(find_word(data_structure, word_to_search))