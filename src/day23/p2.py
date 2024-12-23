data = open("input.txt").read().split("\n")

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

biggest = 0
biggest_party = None
for node in edges.items():
    party = {node[0]}
    for edge in node[1]:
        valid = True
        for to_check in party:
            if to_check not in edges[edge]:
                valid = False
        if valid:
            party.add(edge)

    if len(party) > biggest:
        biggest = len(party)
        biggest_party = party

output = ",".join(sorted(biggest_party))
print(output)
