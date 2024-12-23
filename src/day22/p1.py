nums = list(map(int, open("input.txt").read().split("\n")))

total = 0
for num in nums:
    for i in range(2000):
        res = num * 64
        num = res ^ num
        num = num % 16777216

        res = num // 32
        num = res ^ num
        num = num % 16777216

        res = num * 2048
        num = res ^ num
        num = num % 16777216

    total += num

print(total)
