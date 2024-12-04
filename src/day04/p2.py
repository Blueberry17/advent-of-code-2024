data = open("input.txt").read().split("\n")

total = 0
for line in enumerate(data):
    for char in enumerate(line[1]):
        old = total
        if char[1] == "A":
            if 0 < line[0] < len(data) - 1 and 0 < char[0] < (len(line[1]) - 1):
                x, y = char[0], line[0]
                if data[y-1][x-1] == "M" and data[y+1][x+1] == "S":
                    if data[y-1][x+1] == "M" and data[y+1][x-1] == "S" or \
                            data[y-1][x+1] == "S" and data[y+1][x-1] == "M":
                        total += 1
                elif data[y-1][x-1] == "S" and data[y+1][x+1] == "M":
                    if data[y-1][x+1] == "M" and data[y+1][x-1] == "S" or \
                            data[y-1][x+1] == "S" and data[y+1][x-1] == "M":
                        total += 1

        if old != total:
            print(char[0], line[0], total-old)

print(total)
