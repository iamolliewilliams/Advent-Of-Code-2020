import re

def FileCheck(filename):
    try:
        with open(filename, 'r') as f:
            list_of_passports = [string.split() for string in [string.replace('\n', ' ') for string in f.read().split('\n\n')]]

            list_of_passports_as_dictionaries = []
            for passport in list_of_passports:
                dictionary = {}
                for passport_field in passport:
                    dictionary[passport_field.split(':')[0]] = passport_field.split(':')[1]
                list_of_passports_as_dictionaries.append(dictionary)
                # dictionary.clear()
            return list_of_passports_as_dictionaries
    except:
        return 'Error: Failed to open input file.'

passports = FileCheck('input-files/day4.txt')

def HasFields(passport):
    # byr = birth year, iyr = issue year, eyr = expiration year, hgt = height, hcl = hair color, ecl = eye color, pid = passport id, cid = country id
    return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} <= passport.keys()

def is_passport_valid(passport):
    if HasFields(passport):
        valid_byr = 1920 <= int(passport['byr']) <= 2002
        valid_iyr = 2010 <= int(passport['iyr']) <= 2020
        valid_eyr = 2020 <= int(passport['eyr']) <= 2030
        valid_hgt = True if (passport['hgt'][-2:] == 'cm' and (150 <= int(passport['hgt'][:-2]) <= 193)) or (passport['hgt'][-2:] == 'in' and (59 <= int(passport['hgt'][:-2]) <= 76)) else False
        valid_hcl = True if re.match("^#(?:[0-9a-fA-F]{3}){1,2}$", passport['hcl']) else False
        valid_ecl = passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid_pid = True if re.match("^[0-9]{9}$", passport['pid']) else False
        return valid_byr and valid_iyr and valid_eyr and valid_hgt and valid_hcl and valid_ecl and valid_pid

print('----- Part one -----')
result = len([passport for passport in passports if HasFields(passport)])
print('Number of passports with valid number of fields is {}'.format(result))
print('----- Part two -----')
result = len([passport for passport in passports if is_passport_valid(passport)])
print('Number of valid passports is {}'.format(result))