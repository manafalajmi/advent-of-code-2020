file = open("day-9-input.txt")
contents = file.read().splitlines()

preamble = []

for i in range(25):
    # print(i)
    preamble.append(int(contents[i]))

for i in range(25, len(contents)):
    found = False
    to_test = int(contents[i])
    for num in preamble:

        to_find = to_test - num
        if to_find == num:
            print(num)
            continue
        if to_find in preamble:
            found = True
            break
    if found:
        preamble.append(to_test)
        continue

    print(found)
    print(contents[i])
    break

num_to_sum_to = 133015568  # Solution from part 1

for i in range(len(preamble)):
    sumish = 0
    for j in range(i + 1, len(preamble)):
        sumish += preamble[j]
        if sumish == num_to_sum_to:
            print("found")
            print(i)
            print(j)
            # print(preamble[i] + preamble[j])
            min = min(preamble[i + 1:j + 1])
            max = max(preamble[i + 1:j + 1])
            print(min)
            print(max)
            print(min + max)
        elif sumish > num_to_sum_to:
            break
