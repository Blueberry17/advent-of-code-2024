data = open("input.txt").read().split("\n")

x_lim = len(data[0])
y_lim = len(data)

start = 0+0j
dirs = (1, -1, 1j, -1j)


def valid(current):
    total = 0
    if data[int(current.imag)][int(current.real)] == "9":
        return 1

    for d in dirs:
        new = current+d
        if not (0 <= new.imag < y_lim and 0 <= new.real < x_lim):
            continue
        if int(data[int(current.imag)][int(current.real)]) + 1 == int(data[int(new.imag)][int(new.real)]):
            total += valid(new)

    return total


total = 0
for i in range(y_lim):
    for j in range(x_lim):
        if data[int(start.imag)][int(start.real)] == "0":
            total += valid(start)
        start += 1
    start -= x_lim
    start += 1j

print(total)
