lines = open("input.txt").read().split("\n")

x_lim = 101
y_lim = 103
multiplier = 0
final = set()

while len(final) != len(lines):
    final = set()
    multiplier += 1
    for robot in lines:
        robot = robot.split()
        parts = []
        for part in robot:
            parts.append(list(map(int, part[2:].split(","))))
        final_x = (parts[0][0] + parts[1][0]*multiplier) % x_lim
        final_y = (parts[0][1] + parts[1][1]*multiplier) % y_lim
        final.add((final_x, final_y))

print(multiplier)
