file = open("day1-1 input.txt")
contents = file.read().splitlines()
contents = [int(num) for num in contents]

already_seen = set()
SUM_TO_FIND = 2020

# Day 1 part 1
for num in contents:
    if SUM_TO_FIND - num in already_seen:
        print(num * (SUM_TO_FIND - num))
    already_seen.add(num)

# Day 1 part 2
for i in range(len(contents)):
    first_sum = SUM_TO_FIND - contents[i]
    for j in range(i + 1, len(contents)):
        remainder = first_sum - contents[j]
        if remainder in already_seen:
            print(contents[i] * contents[j] * remainder)
            exit()
