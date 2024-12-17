# print("{:,}".format(8**("2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0".count(","))))

# count = 0
# while True:
#     num = count
#     remainders = []
#     while num > 0:
#         remainders.append(num % 8)
#         num //= 8
#
#     if len(remainders) >= 6:
#         if remainders[:6] == [0,3,5,4,3,0]:
#             print(count)
#             input()
#
#     count += 1
#
# def generate_numbers(divisor, remainders, count=10):
#     base = remainders[0]
#     total = 0
#     for r in reversed(remainders[1:]):
#         total = divisor*(r+total)
#
#     return total+base
#
#
# # Example usage
# divisor = 8
# remainders = [2,4,1,1,7,5,1,5,4,0,5,5,0,3]
# number = generate_numbers(divisor, remainders, count=10)
# for i in range(10):
#     print(number+i*divisor**len(remainders))

import math

lines = open("input.txt").read().split("\n")

def calculate(to_check):
    registers = []
    for register in lines[:3]:
        registers.append(int(register.split()[-1]))

    registers[0] = to_check

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

    return output[:-1]

# part1 = []
# part2 = []
# for i in range(10000):
#     parts = calculate(i).split(",")
#     if len(parts) >= 1 and parts[0] == "2":
#         part1.append(i)
#     if len(parts) >= 2 and parts[0] == "2" and parts[1] == "4":
#         part2.append(i)
# print(part1)
# print(part2)

for i in range(164279024971377, 164279024971552, 1):
    if calculate(i) == "2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0":
        print(i)
        break