def FileCheck(filename):
    try:
        with open(filename, 'r') as f:
            return [string for string in f.read().split('\n')]
    except IOError:
        return 'Error: Failed to open input file.'

list_of_boarding_passes = FileCheck('input-files/day5.txt')

def get_col_row_nums(list_of_passes):
        return [[int(boarding_pass[:7].replace('F', '0').replace('B', '1'),2), int(boarding_pass[-3:].replace('L', '0').replace('R', '1'),2)] for boarding_pass in list_of_passes]

def get_seat_ids(list_of_passes):
    return [boarding_pass[0]*8+boarding_pass[1] for boarding_pass in list_of_passes]

def get_my_seat(list_of_seat_ids):
    sorted_list_of_seat_ids = sorted(list_of_seat_ids)
    for seat_id in sorted_list_of_seat_ids:
        current_index = sorted_list_of_seat_ids.index(seat_id)
        if sorted_list_of_seat_ids[current_index + 1] - sorted_list_of_seat_ids[current_index] == 2:
            return sorted_list_of_seat_ids[current_index] + 1
    return 'Function does not work'

print('----- Part one -----')
rows_and_cols = get_col_row_nums(list_of_boarding_passes)
seat_ids = get_seat_ids(rows_and_cols)
print('Highest seat ID: {}'.format(max(seat_ids)))
print('----- Part two -----')
my_seat_id = get_my_seat(seat_ids)
print('My seat ID is: {}'.format(my_seat_id))