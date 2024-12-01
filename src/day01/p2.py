data = open("input.txt").read().split()

first = []
second = []
for num in enumerate(data):
    if num[0] % 2 == 0:
        first.append(int(num[1]))
    else:
        second.append(int(num[1]))

sim = 0
for num in range(len(first)):
    sim += first[num]*second.count(first[num])
print(sim)
