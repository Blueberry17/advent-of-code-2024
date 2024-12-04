data = open("input.txt").read().split("\n")

total = 0
for line in enumerate(data):
    for char in enumerate(line[1]):
        old = total
        if char[1] == "X":
            if char[0] < (len(line[1])-3) and data[line[0]][char[0]+1:char[0]+4] == "MAS":
                total += 1
            if line[0] < (len(data)-3) and data[line[0]+1][char[0]] == "M" and data[line[0]+2][char[0]] == "A" and \
                  data[line[0]+3][char[0]] == "S":
                total += 1
            if char[0] > 2 and data[line[0]][char[0]-3:char[0]] == "SAM":
                total += 1
            if line[0] > 2 and data[line[0]-1][char[0]] == "M" and data[line[0]-2][char[0]] == "A" and \
                  data[line[0]-3][char[0]] == "S":
                total += 1
            if char[0] < (len(line[1])-3) and line[0] < (len(data)-3) and data[line[0]+1][char[0]+1] == "M" and \
                  data[line[0]+2][char[0]+2] == "A" and data[line[0]+3][char[0]+3] == "S":
                total += 1
            if char[0] > 2 and line[0] > 2 and data[line[0]-1][char[0]-1] == "M" and \
                 data[line[0]-2][char[0]-2] == "A" and data[line[0]-3][char[0]-3] == "S":
                total += 1
            if char[0] > 2 and line[0] < (len(data)-3) and data[line[0]+1][char[0]-1] == "M" and \
                 data[line[0]+2][char[0]-2] == "A" and data[line[0]+3][char[0]-3] == "S":
                total += 1
            if char[0] < (len(line[1])-3) and line[0] > 2 and data[line[0]-1][char[0]+1] == "M" and \
                 data[line[0]-2][char[0]+2] == "A" and data[line[0]-3][char[0]+3] == "S":
                total += 1
        if old != total:
            print(char[0], line[0], total-old)

print(total)
