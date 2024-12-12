data = open("input.txt").read().split()


def identify(coord, char):
    if data[int(coord.imag)][int(coord.real)] == char and coord not in visited:
        coords.append(coord)
        visited.append(coord)
        for vec in [1, -1, 1j, -1j]:
            if 0 <= (coord+vec).real < x_lim and 0 <= (coord+vec).imag < y_lim:
                identify(coord+vec, char)

    return


def calc_bounds(coords):
    xs = []
    ys = []
    for coord in coords:
        xs.append(coord.real)
        ys.append(coord.imag)
    return int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))


visited = []
x_lim = len(data[0])
y_lim = len(data)
cost = 0

for y in range(y_lim):
    for x in range(x_lim):
        if (x*1+y*1j) not in visited:
            coords = []
            identify(x*1+y*1j, data[y][x])

            min_x, min_y, max_x, max_y = calc_bounds(coords)
            perimeter = []
            for coord in coords:
                for vec in [1, -1, 1j, -1j]:
                    if (coord+vec) not in coords:
                        perimeter.append((coord, vec))

            sides = 0

            for vec in [1j, -1j]:
                for yp in range(min_y, max_y+1):
                    last_x = None
                    for xp in range(min_x, max_x+1):
                        if (xp*1+yp*1j, vec) not in perimeter:
                            if last_x:
                                sides += 1
                            last_x = False
                        else:
                            last_x = True
                    if last_x:
                        sides += 1

            for vec in [1, -1]:
                for xp in range(min_x, max_x+1):
                    last_y = None
                    for yp in range(min_y, max_y + 1):
                        if (xp*1+yp*1j, vec) not in perimeter:
                            if last_y:
                                sides += 1
                            last_y = False
                        else:
                            last_y = True
                    if last_y:
                        sides += 1

            cost += len(coords) * sides
print(cost)
