from sympy import symbols, Eq, solve

data = open("input.txt").read().split("\n")

a = []
b = []
p = []

index = 0
while index < len(data)-2:
    parts = data[index].split()
    a.append((int(parts[2][2:-1]), int(parts[3][2:])))
    parts = data[index+1].split()
    b.append((int(parts[2][2:-1]), int(parts[3][2:])))
    parts = data[index+2].split()
    p.append((int(parts[1][2:-1])+10000000000000, int(parts[2][2:])+10000000000000))
    index += 4

total = 0

for i in range(len(a)):
    x, y = symbols('x y', integer=True)

    eq1 = Eq(a[i][0]*x + b[i][0]*y, p[i][0])
    eq2 = Eq(a[i][1]*x + b[i][1]*y, p[i][1])

    try:
        solutions = list(solve((eq1, eq2), (x, y)).values())
        total += solutions[0]*3 + solutions[1]

    except AttributeError:
        pass

print(int(total))
