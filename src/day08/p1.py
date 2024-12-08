import operator

data = open("input.txt").read().split("\n")

x_lim = len(data[0])-1
y_lim = len(data)-1

nodes = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            if char in nodes:
                nodes[char].append((x, y))
            else:
                nodes[char] = [(x, y)]

antinodes = set()
for item in nodes.items():
    nodes, points = item[0], item[1]
    for index, a in enumerate(points):
        for b in points[index+1:]:
            dist1 = tuple(map(operator.sub, a, b))
            dist2 = tuple(map(operator.sub, b, a))
            if dist1[1] < a[1]:
                new_antinodes = (tuple(map(operator.add, a, dist1)), tuple(map(operator.add, b, dist2)))
            else:
                new_antinodes = (tuple(map(operator.add, a, dist2)), tuple(map(operator.add, b, dist1)))
            for antinode in new_antinodes:
                if 0 <= antinode[0] <= x_lim and 0 <= antinode[1] <= y_lim:
                    antinodes.add(antinode)

print(len(antinodes))
