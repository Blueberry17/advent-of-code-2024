from heapq import heappush, heappop

lines = open("input.txt").read().split("\n")

for i in range(1025, len(lines)):
    to_check = lines[:i]

    corrupted = []
    for line in to_check:
        x, y = map(int, line.split(","))
        corrupted.append((x, y))

    target = 70

    grid = []
    for y in range(target+1):
        row = ""
        for x in range(target+1):
            if (x, y) in corrupted:
                row += "#"
            else:
                row += "."
        grid.append(row)

    seen = set()
    pq = [(0, 0, 0, 0, 0, set())]
    costs = {}
    best = float("inf")

    while pq:
        x, y, dx, dy, c, path = heappop(pq)

        if c > best:
            continue

        if x < 0 or x > target or y < 0 or y > target:
            continue

        if x == target and y == target:
            best = c
            continue

        if (x, y) in seen and costs[(x, y)] <= c:
            continue

        seen.add((x, y))
        costs[(x, y)] = c

        for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (ndx, ndy) != (-dx, -dy):
                nx = x + ndx
                ny = y + ndy
                if 0 <= nx <= target and 0 <= ny <= target and grid[ny][nx] != "#":
                    path.add((x, y))
                    heappush(pq, (nx, ny, ndx, ndy, c+1, path))

    if best == float("inf"):
        print(lines[i-1])
        break
