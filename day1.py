def FileCheck(filename):
    try:
        with open(filename) as f:
            return [int(i) for i in f]
    except IOError:
        return 'Error: Failed to open input file.'

list_of_numbers = FileCheck('input-files/day1.txt')

def PartOne(target_num, input_file):
    try:
        num_1 = target_number//2
        possible_numbers = {target_number-x for x in list_of_numbers if x<=num_1} & {x for x in list_of_numbers if x>num_1}
        return [[target_number-x, x] for x in possible_numbers][0]
    except:
        return 'Error: Solution could not be found'

print('----- Part one -----')
target_number = 2020
result = PartOne(target_number, list_of_numbers)
print('Two entries that sum to {} are {} and {}'.format(target_number, result[0], result[1]))
print('Output number is {}'.format(result[0]*result[1]))