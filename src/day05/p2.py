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
    tries = 0
    valid = False
    nums = order.split(",")
    while not valid:
        tries += 1
        valid = True
        new_nums = []
        for index, num in enumerate(nums[1:]):
            if num in rules and nums[index] in rules[num] and valid:
                valid = False
                list_parts = [nums[0:index], nums[index+1], nums[index], nums[index+2:]]
                for part in list_parts:
                    if type(part) == str:
                        new_nums.append(part)
                    else:
                        for x in part:
                            new_nums.append(x)
        if not valid:
            nums = new_nums

    if tries > 1:
        total += int(nums[len(nums)//2])

print(total)
