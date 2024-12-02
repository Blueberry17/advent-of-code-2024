levels = open("input.txt").read().split("\n")

total = 0
for level in levels:
    nums = list(map(int, level.split()))
    diffs = []
    for num in range(len(nums)-1):
        diffs.append(nums[num]-nums[num+1])

    if diffs[0] != 0:
        if diffs[0] > 0:
            positive = True
        else:
            positive = False
        valid = True
        for diff in diffs:
            if (positive and not (1 <= diff <= 3)) or (not positive and not (-3 <= diff <= -1)):
                valid = False
        if valid:
            total += 1

print(total)
