import itertools

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

dx, dy = next(dirs)
total = 1
coords = []
try:
    while True:
        sx += dx
        sy += dy
        if grid[sy][sx] == ".":
            total += 1
            grid[sy][sx] = "X"
        while grid[sy+dy][sx+dx] == "#":
            dx, dy = next(dirs)
        if sy+dy < 0 or sx+dx < 0:
            raise IndexError
        else:
            coords.append((sx, sy))

except IndexError:
    print(total)
    print(coords)
