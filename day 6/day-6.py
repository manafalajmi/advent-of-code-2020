file = open("day-6-input.txt")
contents = file.read().split("\n\n")
contents = [contents.splitlines() for contents in contents]

yes_count = []
total=0
for content in contents:
#     print(content)
    answered_yes = set()
    for person in content:
        for ch in list(person):
            answered_yes.add(ch)
#     print(answered_yes)
    yes_count.append(len(answered_yes))
    total+=len(answered_yes)

# print(total)
# answered_yes = set()
yes_count = []
total = 0
for content in contents:
    this_group = set(list("abcdefghijklmnopqrstuvwxyz"))
    print(this_group)
    for person in content:
        this_person = set()
        for ch in list(person):
            this_person.add(ch)
        print(this_person)
        this_group = this_group.intersection(this_person)

    print(this_group)
    yes_count.append(len(this_group))
    total+=len(this_group)
print(total)