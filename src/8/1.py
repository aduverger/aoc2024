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

antinodes = set()
for char, positions in grid.items():
    for A in positions:
        for B in positions:
            if A == B:
                continue
            d_x = B[0] - A[0]
            d_y = B[1] - A[1]
            antinode = (A[0] - d_x, A[1] - d_y)
            if 0 <= antinode[0] < grid_height and 0 <= antinode[1] < grid_length:
                antinodes.add(antinode)
print(len(antinodes))
