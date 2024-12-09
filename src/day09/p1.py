data = list(map(int, open("input.txt").read()))

frag = ""
num_id = 0
for index, num in enumerate(data):
    if index % 2 == 0:
        for i in range(num):
            frag += str(num_id)
        num_id += 1
    else:
        for i in range(num):
            frag += "."

defrag = []
back = len(frag)-1
front = 0
front_id = 0
last = ""
while front_id <= num_id and front < back:
    if frag[front].isnumeric() and front_id != num_id:
        if int(frag[front:front+len(str(front_id))]) != front_id:
            front_id += 1
        front += len(str(front_id))
        defrag.append(front_id)
        last = ""
    else:
        front += 1
        if last == "":
            front_id += 1
        last = " "
        while not frag[back].isnumeric():
            back -= 1
        if frag[back] != str(num_id)[-1]:
            num_id -= 1
        defrag.append(str(num_id))
        back -= len(str(num_id))

total = 0
for index, num in enumerate(defrag):
    total += index * int(num)
print(total)
