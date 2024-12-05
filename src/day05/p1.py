data = open("input.txt").read().split("\n\n")

rules = {}
for rule in data[0].split("\n"):
    a, b = rule.split("|")
    if a in rules:
        rules[a].append(b)
    else:
        rules[a] = [b]

total = 0
for order in data[1].split("\n"):
    valid = True
    nums = order.split(",")
    for index, num in enumerate(nums[1:]):
        if num in rules and nums[index] in rules[num]:
            valid = False
    if valid:
        total += int(nums[len(nums)//2])

print(total)
