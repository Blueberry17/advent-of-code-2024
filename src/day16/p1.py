from heapq import heappush, heappop

lines = open("input.txt").read().split("\n")

pq = [(1, 139, 1, 0, 0)]
seen = set()
costs = {}
best = float("inf")

while pq:
    x, y, dx, dy, c = heappop(pq)

    if c > best:
        continue

    if x < 0 or x >= len(lines[0]) or y < 0 or y >= len(lines):
        continue

    if x == 139 and y == 1:
        best = c
        break

    if (x, y, dx, dy) in seen and costs[(x, y, dx, dy)] < c:
        continue

    seen.add((x, y, dx, dy))
    costs[(x, y, dx, dy)] = c

    for ndx, ndy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (ndx, ndy) != (-dx, -dy):
            nx = x + ndx
            ny = y + ndy
            if 0 <= nx < len(lines[0]) and 0 <= ny <= len(lines) and lines[ny][nx] != "#":
                if (ndx, ndy) != (dx, dy):
                    dc = 1001
                else:
                    dc = 1
                heappush(pq, (nx, ny, ndx, ndy, c+dc))

print(best)
