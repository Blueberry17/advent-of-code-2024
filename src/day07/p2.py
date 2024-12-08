lines = open("input.txt").read().split("\n")


def combine(total, nums, current):
    if not nums:
        return current == total

    for i in range(0, len(nums)):
        next_num = nums[i]
        if combine(total, nums[i+1:], current+next_num) or combine(total, nums[i+1:], current*next_num) or \
                combine(total, nums[i+1:], int(str(current)+str(next_num))):
            return True
        else:
            return False

    return False

matches = 0
for index, line in enumerate(lines):
    parts = line.split()
    total = int(parts[0][:-1])
    operands = list(map(int, parts[1:]))

    matched = False
    if combine(total, operands[1:], operands[0]):
        matches += total

print(matches)
