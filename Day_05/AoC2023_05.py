import pandas as pd
import re

test_input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4

'''.splitlines()

with open('input.txt', 'r') as f:
    almanac = f.readlines()
    almanac = [x.strip() for x in almanac]
    almanac.append('')

inp = test_input


# Part 1

seeds_pd = pd.DataFrame(columns=['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location'])

seeds = [int(x) for x in re.findall(r'\d+', inp[0].split(': ')[1])]
maps = {x: 0 for x in [x.split(' map:')[0] for x in inp[2:] if ':' in x]}


i = 2
while i < len(inp):
    map_list = []
    if ':' in inp[i]:
        for m in maps.keys():
            if m in inp[i]:
                j = i + 1
                while inp[j] != '':
                    map_list.append([int(x) for x in inp[j].split(' ')])
                    j += 1
                maps[m] = map_list
    i += (j - i) + 1

# print(maps)


def get_ranges(param, curr_source):
    for m in maps.keys():
        if param in m:
            variables = maps[m]
            for v in variables:
                destination, source, ranges = v[0], v[1], v[2]
                if curr_source not in range(source, source + ranges + 1):
                    continue
                else:
                    curr_destination = destination + (curr_source - source)
                    return curr_destination
            return curr_source


for seed in seeds:
    seed_no = seed
    soil_no = get_ranges('-soil', seed_no)
    fertilizer_no = get_ranges('-fertilizer', soil_no)
    water_no = get_ranges('-water', fertilizer_no)
    light_no = get_ranges('-light', water_no)
    temperature_no = get_ranges('-temperature', light_no)
    humidity_no = get_ranges('-humidity', temperature_no)
    location_no = get_ranges('-location', humidity_no)

    seeds_pd = seeds_pd.append({'seed': seed_no, 'soil': soil_no, 'fertilizer': fertilizer_no, 'water': water_no,
                                'light': light_no, 'temperature': temperature_no, 'humidity': humidity_no,
                                'location': location_no},
                               ignore_index=True)

# print(seeds_pd)
print(min(seeds_pd['location']))

#%%
