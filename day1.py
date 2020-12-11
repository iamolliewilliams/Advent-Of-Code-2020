def FileCheck(filename):
    try:
        with open(filename) as f:
            return [int(i) for i in f]
    except IOError:
        return 'Error: Failed to open input file.'

list_of_numbers = FileCheck('input-files/day1.txt')


target_number = 2020
for i, num_1 in enumerate(list_of_numbers):
    num_2 = target_number - num_1
    if num_2 in list_of_numbers[i+1:]:
        print('Two entries that sum to {} are {} and {}'.format(target_number, num_1, num_2))
        print('Output number is {}'.format(num_1*num_2))
        break

