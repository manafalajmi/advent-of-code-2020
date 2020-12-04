import re

def is_valid_passport_with_hack(passport_map, required_fields):
    if len(passport_map) < 7:
        return False
    for field in required_fields:
        if field not in passport_map:
            return False
    return True


def validate_byr(birth_year):
    byr = float(birth_year)
    #loool kids can't fly
    return byr <= 2002 and byr >= 1920


def validate_iyr(issue_year):
    iyr= float (issue_year)
    return iyr<=2020 and iyr>=2010


def validate_hgt(height):
    #will throw errors with bad data lets hope there isnt any
    length = len(height)
    unit = height[length-2: length]
    height_as_number = int(height[0:length-2])
    if unit =='cm':
        return height_as_number <= 193 and height_as_number>=150
    if unit == 'in':
        return height_as_number <= 76 and height_as_number >= 59

    return False

def validate_eyr(expiration_year):
    eyr= float (expiration_year)
    return eyr>=2020 and eyr<=2030


def validate_hcl(hair_color):
    return len(hair_color) == 7 and hair_color[0] == '#' and  hair_color[1:len(hair_color)].isalnum()


def validate_ecl(eye_color):
    allowed_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if eye_color in allowed_colors:
        return True
    return False


def validate_pid(passport_id):
    if len(passport_id) == 9 and float(passport_id):
        return True

def validate_all_fields(passport_map, required_keys_to_function):

    for key in required_keys_to_function.keys():
        if not required_keys_to_function[key](passport_map[key]):
            return False
    return True

REQUIRED_KEYS_TO_FUNCTION = {
    'byr': validate_byr,
    'iyr': validate_iyr,
    'eyr': validate_eyr,
    'hgt': validate_hgt,
    'hcl': validate_hcl,
    'ecl': validate_ecl,
    'pid': validate_pid
}


file = open("day-4-input.txt")
contents = file.read().split('\n\n')
num_of_passwords = len(contents)
contents = [re.split(' |\n', string) for string in contents]

list_of_precheck_valid_maps = []
num_of_valid = 0
for list in contents:
    mappy = {}
    for pair in list:
        if not pair:
            continue
        split_pair = pair.split(':')
        mappy[split_pair[0]] = split_pair[1]

    if is_valid_passport_with_hack(mappy, REQUIRED_KEYS_TO_FUNCTION.keys()):
        # print(mappy)
        list_of_precheck_valid_maps.append(mappy)

# Answer to part 1
print(len(list_of_precheck_valid_maps))

passports_with_valid_fields = 0

for map in list_of_precheck_valid_maps:
    if validate_all_fields(map, REQUIRED_KEYS_TO_FUNCTION):
        passports_with_valid_fields+=1


# Answer to part 2
print(passports_with_valid_fields)
