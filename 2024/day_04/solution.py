def part_one(grid) -> None:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    word = "XMAS"
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                found = True
                for k in range(len(word)):
                    x, y = i + k * dx, j + k * dy
                    if not (0 <= x < rows and 0 <= y < cols) or grid[x][y] != word[k]:
                        found = False
                        break
                if found:
                    count += 1

    print(f"Total occurrences of '{word}': {count}")


def is_xmas_pattern(i, j):
    if grid[i][j] != "A":
        return False

    d1 = grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S"
    d1r = grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M"
    d2 = grid[i - 1][j + 1] == "M" and grid[i + 1][j - 1] == "S"
    d2r = grid[i - 1][j + 1] == "S" and grid[i + 1][j - 1] == "M"

    if (d1 and d2) or (d1r and d2r) or (d1 and d2r) or (d1r and d2):
        return True

    return False


def part_two(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(1, rows - 1):  # Exclude the edges
        for j in range(1, cols - 1):  # Exclude the edges
            if grid[i][j] == "A" and is_xmas_pattern(i, j):
                count += 1

        print(f"Total occurrences of 'X-MAS': {count}")


if __name__ == "__main__":

    with open("input.txt") as input_file:
        grid = [line.strip() for line in input_file]
        part_one(grid)
        part_two(grid)
