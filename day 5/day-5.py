file = open("day-5-input.txt")
contents = file.read().splitlines()
NUM_OF_ROWS = 128
NUM_OF_COLUMNS = 8
POSSIBLE_SEATS = NUM_OF_ROWS * NUM_OF_COLUMNS
ROW_CODE_TYPE = 'ROW'
COLUMN_CODE_TYPE = 'COLUMN'


def getSeatId(seat_code):
    row = get_row(seat_code[0:7])
    col = get_column(seat_code[7:len(seat_code)])
    return row * 8 + col


def get_row(seat_code):
    return get_code_value(seat_code, 'B', 'F', 127, 0)


def get_column(seat_code):
    return get_code_value(seat_code, 'R', 'L', 7, 0)


def get_code_value(row_code, high_code, low_code, high_range, low_range):
    for i in range(len(row_code)):
        diff = ((high_range - low_range) + 1) / 2

        if row_code[i] == low_code:
            high_range -= diff
        if row_code[i] == high_code:
            low_range += diff

    return low_range if row_code[len(row_code) - 1] == low_code else high_range


def find_all_seat_ids():
    list = []
    for line in contents:
        curr_seat = getSeatId(line)
        list.append(int(curr_seat))
    return list


def find_max_seat_id(list_of_ids):
    curr_max = 0
    for curr_seat in list_of_ids:
        curr_max = curr_max if curr_max > curr_seat else curr_seat
    return curr_max


def find_my_seat(list_of_seats):
    excluded_seats = {0, 1, 2, 3, 4, 5, 6, 7, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023}
    used_seats = set(list_of_seats)
    used_seats = used_seats | excluded_seats
    possible_seats = set([i for i in range(POSSIBLE_SEATS)])
    my_possible_seats = possible_seats.difference(used_seats)
    for seat in my_possible_seats:  # my seats adjacent seats have people in them, and I'm not in the first/last row
        if seat + 1 in used_seats and seat - 1 in used_seats:
            return seat


def solution():
    list_of_seats = find_all_seat_ids()
    print(find_max_seat_id(list_of_seats))
    print(find_my_seat(list_of_seats))


solution()
