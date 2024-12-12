import functools

data = list(map(int, open("input.txt").read().split()))

def calc_new(num):
    to_add = []
    if num == 0:
        to_add.append(1)
    elif len(str(num)) % 2 == 0:
        num = str(num)
        to_add.append(int(num[:len(num) // 2]))
        to_add.append(int(num[len(num) // 2:]))
    else:
        to_add.append(num * 2024)

    return to_add

@functools.cache
def expand(num, remaining=76):
    if remaining == 1:
        return 1

    remaining -= 1
    to_add = calc_new(num)
    if len(to_add) > 1:
        return expand(to_add[0], remaining) + expand(to_add[1], remaining)
    else:
        return expand(to_add[0], remaining)

total = 0
for num in data:
    total += expand(num)
print(total)
