inits, gates = open("input.txt").read().split("\n\n")

states = {}
for init in inits.split("\n"):
    wire, state = init.split()
    states[wire[:-1]] = int(state)

operations = {"AND": "&", "OR": "|", "XOR": "^"}
gates = gates.split("\n")
zs = {}
while gates:
    gate = gates.pop(0)
    s1, operation, s2, _, s3 = gate.split()
    if s1 in states and s2 in states:
        exec(f"states['{s3}'] = states['{s1}'] {operations[operation]} states['{s2}']")
        if s3[0] == "z":
            exec(f"zs['{s3}'] = states['{s1}'] {operations[operation]} states['{s2}']")
    else:
        gates.append(gate)

zs = dict((sorted(zs.items())))
num = 0
exp = 0
for z in zs:
    if zs[z] == 1:
        num += 2 ** exp
    exp += 1
print(num)
