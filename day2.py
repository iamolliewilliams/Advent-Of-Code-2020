import re

def FileImport(filename):
    password_parameters = []
    try:
        for line in open(filename).readlines():
            policy = re.findall(r'\w+', line)
            password_parameters.append([int(policy[0]), int(policy[1]), policy[2], policy[3]])
        return password_parameters
    except IOError:
        return 'Error: Failed to open input file.'

def PartOne(list_of_policies):
    count = 0
    for policy in list_of_policies:
        if policy[0] <= policy[3].count(policy[2]) <= policy[1]:
            count += 1
    return count

def PartTwo(list_of_policies):
    count = 0
    for policy in list_of_policies:
        if (policy[3][policy[0]-1] == policy[2]) != (policy[3][policy[1]-1] == policy[2]):
            count += 1
    return count

list_of_policies = FileImport('input-files/day2.txt')


print('----- Part one -----')
result = PartOne(list_of_policies)
print('Total number of valid passwords are {}'.format(result))
print('----- Part two -----')
result = PartTwo(list_of_policies)
print('Total number of valid passwords are {}'.format(result))
