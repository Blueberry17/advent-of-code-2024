data = open("input.txt").read().split("\n\n")

grid = []
for y, line in enumerate(data[0].split("\n")):
    row = []
    for x, char in enumerate(line):
        if char == "@":
            sx, sy = x*2, y
            row.append("@")
            row.append(".")
        elif char == "." or char == "#":
            row.append(char)
            row.append(char)
        else:
            row.append("[")
            row.append("]")

    grid.append(row)


def push_h(x, y, dx, dy):
    x += dx
    if grid[y][x] == "#":
        return False
    if grid[y][x] == ".":
        return True
    if push_h(x, y, dx, dy):
        grid[y+dy][x+dx] = grid[y][x]
        return True
    return False


def push_y(x, y, dy):
    y += dy
    if grid[y][x] == "#":
        return False
    if grid[y][x] == ".":
        return True
    if grid[y][x] == "[":
        if push_y(x, y, dy) and push_y(x+1, y, dy):
            to_change[(y+dy, x)] = grid[y][x]
            to_change[(y+dy, x+1)] = grid[y][x+1]
            if (y, x+1) not in to_change:
                to_change[(y, x+1)] = "."
            return True
        return False
    if push_y(x, y, dy) and push_y(x-1, y, dy):
        to_change[(y + dy, x)] = grid[y][x]
        to_change[(y + dy, x - 1)] = grid[y][x - 1]
        if (y, x-1) not in to_change:
            to_change[(y, x - 1)] = "."
        return True
    return False


ds = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
for iteration, d in enumerate(data[1].replace("\n", "")):
    dx, dy = ds[d]
    if grid[sy+dy][sx+dx] == ".":
        grid[sy+dy][sx+dx] = "@"
        grid[sy][sx] = "."
        sx += dx
        sy += dy
    elif grid[sy+dy][sx+dx] == "[" or grid[sy+dy][sx+dx] == "]":
        if dy == 0:
            if push_h(sx, sy, dx, dy):
                grid[sy][sx] = "."
                grid[sy+dy][sx+dx] = "@"
                sx += dx
                sy += dy
        else:
            to_change = {}
            if push_y(sx, sy, dy):
                for i in to_change.items():
                    grid[i[0][0]][i[0][1]] = i[1]
                grid[sy][sx] = "."
                grid[sy+dy][sx+dx] = "@"
                sx += dx
                sy += dy

total = 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "[":
            l, r, t, b = x-1, len(line)-3-x, y, len(grid)-1-y
            total += y*100+x

print(total)
