import operator

data = open("input.txt").read().split("\n")

x_lim = len(data[0])-1
y_lim = len(data)-1

nodes = {}
dists = {}
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            new_dists = []
            for node in nodes:
                if node == char:
                    for node_tuple in nodes[node]:
                        new_dists.append(tuple(map(operator.sub, node_tuple, (x, y))))
            dists[(x, y)] = new_dists
            if char in nodes:
                nodes[char].append((x, y))
            else:
                nodes[char] = [(x, y)]

antinodes = set()
for dist in dists.items():
    a, ds = dist[0], dist[1]
    for d in ds:
        neg_dir = pos_dir = True
        count = 0
        while neg_dir or pos_dir:
            new_antinodes = [tuple(map(operator.sub, a, tuple(count*x for x in d))),
                             tuple(map(operator.add, a, tuple(count*x for x in d)))]
            count += 1
            for index, antinode in enumerate(new_antinodes):
                if 0 <= antinode[0] <= x_lim and 0 <= antinode[1] <= y_lim:
                    antinodes.add(antinode)
                else:
                    if index == 0:
                        neg_dir = False
                    else:
                        pos_dir = False

print(len(antinodes))
