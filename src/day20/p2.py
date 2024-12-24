grid = open("input.txt").read().split("\n")

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def valid(x, y, mat):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y] != '#'


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def walk(start, end, grid, dist):
    p = end
    x = end
    c = 0
    while start != x:
        dist[x] = c
        c += 1
        for d in directions:
            u = (x[0] + d[0], x[1] + d[1])
            if u != p and valid(*u, grid):
                p = x
                x = u
                break
    dist[start] = c
    return dist[start]

start = (0, 0)
end = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'E':
            end = (i, j)

dist = {}

walk(start, end, grid, dist)

count = 0
for k, v in reversed(dist.items()):
    for k2, v2 in dist.items():
        d = manhattan(k, k2)
        if d <= 20 and v2 - v - d >= 100:
            count += 1
print(count)
