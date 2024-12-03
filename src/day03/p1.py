import re

data = open("input.txt").read()

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
total = 0
for match in matches:
    a, b = map(int, re.search(r"\d{1,3},\d{1,3}", match).group(0).split(','))
    total += a*b
print(total)
