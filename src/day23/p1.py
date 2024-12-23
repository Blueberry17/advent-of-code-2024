import itertools

data = open("example.txt").read().split("\n")

seen = set()
edges = {}
for line in data:
    nodes = line.split("-")
    for node in nodes:
        if node not in seen:
            seen.add(node)
            edges[node] = []
    edges[nodes[0]].append(nodes[1])
    edges[nodes[1]].append(nodes[0])

parties = set()
for node in edges.items():
    to_check = itertools.combinations(node[1], 2)
    for edge in to_check:
        if edge[1] in edges[edge[0]]:
            party = (node[0], edge[0], edge[1])
            valid = False
            for pos in party:
                if pos[0] == "t":
                    valid = True
            if not valid:
                continue
            party = tuple(sorted(party))
            parties.add(party)

print(len(parties))
