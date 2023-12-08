import re

test_input = '''Time:      7  15   30
Distance:  9  40  200'''.splitlines()

with open('input.txt', 'r') as f:
    records = f.readlines()

times = [int(x) for x in re.findall(r'\d+', records[0])]
distances = [int(x) for x in re.findall(r'\d+', records[1])]

# Part 1

tot_margin = 1

for time, distance in zip(times, distances):
    margin_of_error = 0
    for i in range(1, time):
        dist = time*i-i**2
        if dist > distance:
            margin_of_error +=1
    tot_margin *= margin_of_error

print(f'Total margin of error: {tot_margin}.\n')
