import math

lines = open("input.txt").read().split("\n")

registers = []
for register in lines[:3]:
    registers.append(int(register.split()[-1]))


def combos(num):
    combs = {0: 0, 1: 1, 2: 2, 3: 3, 4: registers[0], 5: registers[1], 6: registers[2]}
    return combs[num]

program = list(map(int, lines[-1].split()[1].split(",")))
output = ""

pointer = -2
while pointer < len(program)-3:
    pointer += 2
    opc, opr = program[pointer], program[pointer+1]
    if opc == 0:
        registers[0] = math.trunc(registers[0] / 2**combos(opr))
    elif opc == 1:
        registers[1] = registers[1] ^ opr
    elif opc == 2:
        registers[1] = combos(opr) % 8
    elif opc == 3:
        if registers[0] != 0:
            pointer = opr - 2
    elif opc == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opc == 5:
        output += f"{combos(opr) % 8},"
    elif opc == 6:
        registers[1] = math.trunc(registers[0] / 2**combos(opr))
    elif opc == 7:
        registers[2] = math.trunc(registers[0] / 2 ** combos(opr))

print(output[:-1])
