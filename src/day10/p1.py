data = open("input.txt").read().split("\n")

x_lim = len(data[0])
y_lim = len(data)

start = 0+0j
dirs = (1, -1, 1j, -1j)


def valid(current, seen):
    total = 0
    if data[int(current.imag)][int(current.real)] == "9":
        if current not in seen:
            seen.add(current)
            return 1
        else:
            return 0

    for d in dirs:
        new = current+d
        if not (0 <= new.imag < y_lim and 0 <= new.real < x_lim):
            continue
        if int(data[int(current.imag)][int(current.real)]) + 1 == int(data[int(new.imag)][int(new.real)]):
            total += valid(new, seen)

    return total


total = 0
for i in range(y_lim):
    for j in range(x_lim):
        if data[int(start.imag)][int(start.real)] == "0":
            total += valid(start, set())
        start += 1
    start -= x_lim
    start += 1j

print(total)
