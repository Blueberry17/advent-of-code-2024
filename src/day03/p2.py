import re

data = open("input.txt").read()

matches = list(re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data))

total = 0
enabled = True
for match in matches:
    if match == "do()":
        enabled = True
    elif match == "don't()":
        enabled = False
    elif enabled:
        a, b = map(int, re.search(r"\d{1,3},\d{1,3}", match).group(0).split(','))
        total += a*b
print(total)
