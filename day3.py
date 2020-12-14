def FileCheck(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().split('\n')
    except:
        return 'Error: Failed to open input file.'

input_map = FileCheck('input-files/day3.txt')
# all strings in map are 31 characters long

def does_tree_exist_at_coordinate(x_coordinate, y_coordinate):
    x = x_coordinate % 31
    return input_map[y_coordinate][x] == '#'

def count_trees_on_route(slope_right, slope_down):
    right_coordinate = 0
    down_coordinate = 0
    num_of_trees = 0

    while down_coordinate < len(input_map):
        if does_tree_exist_at_coordinate(right_coordinate, down_coordinate):
            num_of_trees += 1
        right_coordinate += slope_right
        down_coordinate += slope_down
    return num_of_trees

print('----- Part one -----')
result = count_trees_on_route(3, 1)
print('Number of trees on route is {}'.format(result))
print('----- Part two -----')
result = result * count_trees_on_route(1, 1) * count_trees_on_route(5, 1) * count_trees_on_route(7, 1) * count_trees_on_route(1, 2)
print('Multiplied value of trees on route(1,1), route(3,1), route(5,1), route(7,1) and route(1,2) is {}'.format(result))
