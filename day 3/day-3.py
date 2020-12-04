file = open("input-day-3.txt")
contents = file.read().splitlines()
num_of_rows = len(contents)
num_of_cols = len(contents[0])
def follow_slope(x_step, y_step):
    x=x_step
    y=y_step
    num_of_trees = 0
    while (x < num_of_rows):
        if contents[x][y % num_of_cols] == '#':
            num_of_trees += 1
        x += x_step
        y += y_step
    return num_of_trees
# contents = [string.split() for string in contents]


one = follow_slope(1,1)
two = follow_slope(1,3)
three = follow_slope(1,5)
four = follow_slope(1,7)
five = follow_slope(2,1)

combination = one * two * three * four * five
print(combination)


