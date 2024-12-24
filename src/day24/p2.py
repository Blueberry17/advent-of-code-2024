inits, gates = open("input.txt").read().split("\n\n")

states = {}
xs = {}
ys = {}
for init in inits.split("\n"):
    wire, state = init.split()
    states[wire[:-1]] = int(state)
    if wire[0] == "x":
        xs[wire[:-1]] = int(state)
    elif wire[0] == "y":
        ys[wire[:-1]] = int(state)

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
nums = []
for var in [xs, ys, zs]:
    num = 0
    exp = 0
    for bit in var:
        if var[bit] == 1:
            num += 2 ** exp
        exp += 1
    nums.append(num)

target = bin(nums[1]+nums[0])
current = bin(nums[2])

print(target)
print(current)
for i in range(2, len(target)):
    if target[i] != current[i]:
        print(1, end="")
    else:
        print(0, end="")
print()

carry = 0
for i in range(len(xs)):
    total = ys[f"y{str(i).zfill(2)}"] + xs[f"x{str(i).zfill(2)}"] + carry
    if total == 3 and zs[f"z{str(i).zfill(2)}"] != 1:
        print(i, 3, zs[f"z{str(i).zfill(2)}"])
    if total == 2 and zs[f"z{str(i).zfill(2)}"] != 0:
        print(i, 2, zs[f"z{str(i).zfill(2)}"])
    if total == 1 and zs[f"z{str(i).zfill(2)}"] != 1:
        print(i, 1, zs[f"z{str(i).zfill(2)}"])
    if total > 1:
        carry = 1
    else:
        carry = 0

# ckj,dbp,fdv,kdf,rpp,z15,z23,z39
