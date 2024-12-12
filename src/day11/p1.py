import copy

data = list(map(int, open("input.txt").read().split()))

for i in range(25):
    new_data = []
    for num in data:
        if num == 0:
            new_data.append(1)
        elif len(str(num)) % 2 == 0:
            num = str(num)
            new_data.append(int(num[:len(num)//2]))
            new_data.append(int(num[len(num)//2:]))
        else:
            new_data.append(num*2024)

    data = copy.deepcopy(new_data)

print(len(new_data))
