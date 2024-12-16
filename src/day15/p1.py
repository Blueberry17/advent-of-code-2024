data = open("input.txt").read().split("\n\n")

grid = []
for y, line in enumerate(data[0].split("\n")):
    row = []
    for x, char in enumerate(line):
        row.append(char)
        if char == "@":
            sx, sy = x, y
    grid.append(row)


def push(x, y, dx, dy):
    x += dx
    y += dy
    if grid[y][x] == "#":
        return False
    if grid[y][x] == ".":
        return True
    if push(x, y, dx, dy):
        grid[y+dy][x+dx] = "O"
        grid[y][x] = "."
        return True
    return False


ds = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
for d in data[1].replace("\n", ""):
    dx, dy = ds[d]
    if grid[sy+dy][sx+dx] == ".":
        grid[sy+dy][sx+dx] = "@"
        grid[sy][sx] = "."
        sx += dx
        sy += dy
    elif grid[sy+dy][sx+dx] == "O":
        if push(sx, sy, dx, dy):
            grid[sy][sx] = "."
            grid[sy+dy][sx+dx] = "@"
            sx += dx
            sy += dy

total = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "O":
            total += (y*100+x)

print(total)