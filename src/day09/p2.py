data = list(map(int, open("input.txt").read()))

files = {}
frag = []
num_id = 0
for index, num in enumerate(data):
    if index % 2 == 0:
        for i in range(num):
            files[str(num_id)] = num
        frag.append(num_id)
        num_id += 1
    else:
        frag.append("."*num)

defrag = []
back = len(frag)-1
front = 0
front_id = 0
back_id = max(map(int, files.keys()))

while front_id <= back_id and front < back and len(files) > 0:
    if str(frag[front]).isnumeric():
        while str(front_id) not in files:
            front_id += 1
        for i in range(files[str(front_id)]):
            defrag.append(front_id)
        del files[str(front_id)]
        front_id += 1
        front += 1

    elif len(frag[front]) > 0:
        gap = len(frag[front])
        file_space = 1000
        tried = 1
        while gap < file_space and back_id+tried > 0:
            tried -= 1
            target_file = str(back_id+tried)
            if target_file in files:
                file_space = files[target_file]
        if gap >= file_space:
            residual = gap - file_space
            for i in range(file_space):
                defrag.append(target_file)
            frag[front] = residual * "."
            frag_index = frag.index(int(target_file))
            frag[frag_index] = files[target_file] * "."
            del files[target_file]
        else:
            for i in range(gap):
                defrag.append(0)
            front += 1

    else:
        front += 1

total = 0
for index, num in enumerate(defrag):
    total += index * int(num)
print(total)
