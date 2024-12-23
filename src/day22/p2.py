nums = list(map(int, open("input.txt").read().split("\n")))

all_sequences = {}
for num in nums:
    changes = []
    prices = []
    sequences = []
    last = int(str(num)[-1])

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

        if last is not None:
            changes.append(int(str(num)[-1]) - last)
        last = int(str(num)[-1])
        prices.append(last)

    for index in range(0, len(changes)-3):
        sequence = (changes[index], changes[index+1], changes[index+2], changes[index+3])
        if sequence in sequences:
            continue
        sequences.append(sequence)
        if sequence in all_sequences:
            all_sequences[sequence] += prices[index+3]
        else:
            all_sequences[sequence] = prices[index+3]

key_with_max_value = max(all_sequences, key=all_sequences.get)
print(all_sequences[key_with_max_value])
