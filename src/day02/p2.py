levels = open("input.txt").read().split("\n")

total = 0


def calculate_diffs(nums):
    diffs = []
    for num in range(len(nums)-1):
        diffs.append(nums[num]-nums[num+1])

    return diffs


def diff_type(diffs):
    pos_diffs = neg_diffs = non_diffs = big_diffs = 0
    for diff in diffs:
        if 1 <= diff <= 3:
            pos_diffs += 1
        elif -3 <= diff <= -1:
            neg_diffs += 1
        elif diff == 0:
            non_diffs += 1
        else:
            big_diffs += 1

    return pos_diffs, neg_diffs, non_diffs, big_diffs


for level in levels:
    nums = list(map(int, level.split()))
    skip = False

    for index in range(len(nums)):
        if skip:
            continue

        new_nums = nums.copy()
        new_nums.pop(index)

        diffs = calculate_diffs(new_nums)
        pos_diffs, neg_diffs, non_diffs, big_diffs = diff_type(diffs)

        if pos_diffs == len(diffs) or neg_diffs == len(diffs):
            total += 1
            skip = True

print(total)
