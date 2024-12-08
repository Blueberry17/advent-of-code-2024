import itertools
import copy

data = open("input.txt").read().split("\n")

grid = []
for y, line in enumerate(data):
    row = []
    for x, char in enumerate(line):
        if char == "^":
            sx, sy = x, y
            row.append("X")
        else:
            row.append(char)
    grid.append(row)

dirs = itertools.cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])

fx, fy = sx, sy
cycles = 0

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        new_grid = copy.deepcopy(grid)
        if new_grid[y][x] == "#" or y == fy and x == fx or y == (fy-1) and x == fx:
            continue
        new_grid[y][x] = "O"

        dirs = itertools.cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
        dx, dy = next(dirs)
        total = 0

        try:
            seen = {(fx, fy): 1}
            sx, sy = fx, fy
            seen_total = 0
            total = 0
            while True:
                total += 1
                sx += dx
                sy += dy

                if (sx, sy) in seen:
                    seen[(sx, sy)] += 1
                    if seen[(sx, sy)] > 4:
                        cycles += 1
                        raise IndexError
                else:
                    seen[(sx, sy)] = 0

                if new_grid[sy][sx] == ".":
                    new_grid[sy][sx] = "X"

                if sy+dy < 0 or sx+dx < 0:
                    raise IndexError

                while new_grid[sy+dy][sx+dx] == "#" or new_grid[sy+dy][sx+dx] == "O":
                    dx, dy = next(dirs)

        except IndexError as e:
            # print(cycles, y*len(line)+(x+1), len(grid)*len(grid[0]))
            pass
