file = open("day-2-input.txt")
contents = file.read().splitlines()
num_of_passwords = len(contents)
contents = [string.split(" ") for string in contents]

#part 1
num_of_invalid_passwords =0
for i in range(num_of_passwords):
    occurence_range = contents[i][0].split("-")
    key = contents[i][1][0]
    password = contents[i][2]
    occurence_count = password.count(key)

    if occurence_count< int(occurence_range[0]) or occurence_count> int(occurence_range[1]):
        num_of_invalid_passwords+=1

print(num_of_passwords- num_of_invalid_passwords)


# part 2

num_of_valid_passwords =0
for i in range(num_of_passwords):
    occurence_location = contents[i][0].split("-")
    key = contents[i][1][0]
    password = contents[i][2]

    occurs_first = password[int(occurence_location[0]) -1] == key
    occurs_second = password[int(occurence_location[1]) -1] == key
    if  occurs_first^ occurs_second :
        num_of_valid_passwords+=1

print(num_of_valid_passwords)

