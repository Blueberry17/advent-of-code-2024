lines = open("input.txt").read().split("\n")

match = 0
for line in lines:
    matched = False
    nums = line.split()
    total = int(nums[0][:-1])
    operands = list(map(int, nums[1:]))

    combs = []
    for i in range(2**(len(operands)-1)):
        combs.append(bin(i)[2:].zfill(len(operands)-1))
    operators = "+*"

    for comb in combs:
        expression = operands[0]
        for index, operand in enumerate(operands[1:]):
            exec(f"expression {operators[int(comb[index])]}= {operand}")
        if expression == total:
            matched = True

    if matched:
        match += total

print("TOTAL", match)
