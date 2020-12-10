file = open("day-7-input.txt")
contents = file.read().splitlines()
contents = [contents.split("contain") for contents in contents]
contains_map = {}
contained_in_map = {}
for rule in contents:
    bag_type = rule[0].strip().split()
    bag_color = bag_type[0] + " " + bag_type[1]
    contains = set()
    print(bag_color)
    for inner_bag in rule[1].strip().split(","):
        quantity = int(inner_bag[0])
        inner_bag_name = inner_bag[1] + " " + inner_bag[2]
        print(inner_bag_name)
        contains.add(inner_bag_name)
