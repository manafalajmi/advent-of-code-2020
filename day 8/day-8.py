file = open("day-8-input.txt")
contents = file.read().splitlines()
contents = [content.split() for content in contents]

accumulator = 0
pointer = 0
instructions_seen = set()
how_many_seen = 0

while (how_many_seen<6):

    if(pointer in instructions_seen):
        print(pointer)
        print(contents[pointer])
        # how_many_seen+=1
    instructions_seen.add(pointer)

    if contents[pointer][0] == "acc":
        accumulator += int(contents[pointer][1])
        pointer+=1
    elif contents[pointer][0] == "jmp":
        pointer += int(contents[pointer][1])
    elif contents[pointer][0] == "nop":
        pointer += 1

print(accumulator)
print(pointer)
print(contents[pointer])