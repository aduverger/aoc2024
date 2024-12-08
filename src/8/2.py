from collections import defaultdict


with open("./input.txt", "r") as file:
    grid = defaultdict(list)
    for row, line in enumerate(file.readlines()):
        line = line.strip()
        grid_length = len(line)
        for col, char in enumerate(line):
            if char != ".":
                grid[char].append((row, col))
    grid_height = row + 1


def is_in_grid(antinode, grid_height, grid_length):
    return 0 <= antinode[0] < grid_height and 0 <= antinode[1] < grid_length


antinodes = set()
for char, positions in grid.items():
    for A in positions:
        for B in positions:
            if A == B:
                continue
            d_x = B[0] - A[0]
            d_y = B[1] - A[1]
            for alpha in range(max(grid_height, grid_length)):
                antinode = (A[0] - alpha * d_x, A[1] - alpha * d_y)
                if not is_in_grid(antinode, grid_height, grid_length):
                    break
                antinodes.add(antinode)

print(len(antinodes))
