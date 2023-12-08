test_input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''.splitlines()

# Part 1

with open('input.txt', 'r') as f:
    calibration_values = f.readlines()

calibration_sum = 0
for line in calibration_values:
    digits = [d for d in line if d.isdigit()]
    if len(digits) != 2:
        digits = [digits[0], digits[-1]]
    calibration_sum += int(''.join(digits))

print(f'The sum of all of the calibration values is {calibration_sum}.')

# Part 2

import re

digits_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
               '1', '2', '3', '4', '5', '6', '7', '8', '9']

digits_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

test_input_2 = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''.splitlines()

calibration_sum = 0

for line in calibration_values:
    # print(line)
    min_ind, max_ind = [len(line)-1, 0], [0, 0]
    for digit in digits_list:
        pattern = f'(?={digit})'
        indexes = [m.start() for m in re.finditer(pattern, line)]
        for ind in indexes:
            if ind <= min_ind[0]:
                min_ind[0] = ind
                min_ind[1] = digits_dict.get(digit, digit)
            if ind >= max_ind[0]:
                max_ind[0] = ind
                max_ind[1] = digits_dict.get(digit, digit)
    # print(min_ind, max_ind)
    calibration_value = int(''.join([min_ind[1], max_ind[1]]))
    # print(calibration_value)

    calibration_sum += calibration_value


print(f'The sum of all of the calibration is {calibration_sum}.')
#%%
