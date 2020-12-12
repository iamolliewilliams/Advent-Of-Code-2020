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

def PartTwo(target_num, input_file):
    for num_1 in range(len(input_file)):
        for num_2 in range(num_1+1, len(input_file)):
            for num_3 in range(num_2+1, len(input_file)):
                if input_file[num_1]+input_file[num_2]+input_file[num_3] == target_num:
                    return [input_file[num_1], input_file[num_2], input_file[num_3]]


target_number = 2020
print('----- Part one -----')
result = PartOne(target_number, list_of_numbers)
print('Two entries that sum to {} are {} and {}'.format(target_number, result[0], result[1]))
print('Output number is {}'.format(result[0]*result[1]))
print('----- Part two -----')
result = PartTwo(target_number, list_of_numbers)
print('Three entries that sum to {} are {}, {} and {}'.format(target_number, result[0], result[1], result[2]))
print('Output number is {}'.format(result[0]*result[1]*result[2]))