file = open("day-8-input.txt")
contents = file.read().splitlines()
contents = [content.split() for content in contents]


def find_all_jmps_and_nops(content_arr):
    copied_contents = content_arr
    jmp_indices = []
    nop_indices = []
    for i in range(len(content_arr)):
        if content_arr[i][0] == "jmp":
            jmp_indices.append(i)
        if content_arr[i][0] == "nop":
            nop_indices.append(i)

    for index in jmp_indices:
        copied_contents[index][0] = "nop"
        acc = did_it_reach_the_end(copied_contents)
        if acc != 0:
            return acc
        else:
            copied_contents[index][0] = "jmp"

    for index in nop_indices:
        copied_contents[index][0] = "jmp"
        acc = did_it_reach_the_end(copied_contents)
        if acc != 0:
            return acc
        else:
            copied_contents[index][0] = "nop"


def did_it_reach_the_end(content_arr):
    accumulator = 0
    pointer = 0
    instructions_seen = set()
    pointers_in_order = []
    how_many_seen = 0

    while (how_many_seen < 6):
        pointers_in_order.append(pointer)
        if (pointer in instructions_seen):
            how_many_seen += 1
        instructions_seen.add(pointer)

        if content_arr[pointer][0] == "acc":
            accumulator += int(content_arr[pointer][1])
            pointer += 1
        elif content_arr[pointer][0] == "jmp":
            pointer += int(content_arr[pointer][1])
        elif content_arr[pointer][0] == "nop":
            pointer += 1

        if pointer == len(content_arr) - 1:
            print("hello I find maybe")
            print(accumulator)
            return accumulator
    # print(pointers_in_order)
    return 0


find_all_jmps_and_nops(contents)
