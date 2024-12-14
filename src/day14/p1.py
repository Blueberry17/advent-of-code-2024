lines = open("input.txt").read().split("\n")

x_lim = 101
y_lim = 103

final = []

for robot in lines:
    robot = robot.split()
    parts = []
    for part in robot:
        parts.append(list(map(int, part[2:].split(","))))
    final_x = (parts[0][0] + parts[1][0]*100) % x_lim
    final_y = (parts[0][1] + parts[1][1]*100) % y_lim
    final.append([final_x, final_y])

a = b = c = d = 0
for (x, y) in final:
    if x < x_lim//2:
        if y < y_lim//2:
            a += 1
        elif y > y_lim/2:
            b += 1
    elif x > x_lim/2:
        if y < y_lim//2:
            c += 1
        elif y > y_lim/2:
            d += 1

print(a*b*c*d)
