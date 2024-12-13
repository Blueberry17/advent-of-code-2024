data = open("input.txt").read().split("\n")

a = []
b = []
p = []

index = 0
while index < len(data)-2:
    parts = data[index].split()
    a.append(int(parts[2][2:-1]) + int(parts[3][2:])*1j)
    parts = data[index+1].split()
    b.append(int(parts[2][2:-1]) + int(parts[3][2:])*1j)
    parts = data[index+2].split()
    p.append(int(parts[1][2:-1]) + int(parts[2][2:])*1j)
    index += 4

total = 0
for i in range(len(a)):
    smallest = float("inf")
    smallest_a = smallest_b = 0
    for j in range(101):
        start = a[i]*j
        if abs(((p[i]-start)/b[i]).imag) < 0.0001:
            presses = j*3+((p[i]-start)/b[i]).real
            if presses < smallest:
                smallest = presses
                smallest_a = j
                smallest_b = ((p[i]-start)/b[i]).real
    if smallest != float("inf"):
        total += smallest
print(int(total))
