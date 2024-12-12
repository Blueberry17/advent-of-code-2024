data = open("input.txt").read().split()


def identify(coord, char):
    if data[int(coord.imag)][int(coord.real)] == char and coord not in visited:
        coords.append(coord)
        visited.append(coord)
        for vec in [1, -1, 1j, -1j]:
            if 0 <= (coord+vec).real < x_lim and 0 <= (coord+vec).imag < y_lim:
                identify(coord+vec, char)

    return


visited = []
x_lim = len(data[0])
y_lim = len(data)
cost = 0

for y in range(y_lim):
    for x in range(x_lim):
        if (x*1+y*1j) not in visited:
            coords = []
            identify(x*1+y*1j, data[y][x])
            perimeter = 0
            for coord in coords:
                total = 4
                for vec in [1, -1, 1j, -1j]:
                    if (coord+vec) in coords:
                        total -= 1
                perimeter += total
            cost += len(coords) * perimeter

print(cost)
