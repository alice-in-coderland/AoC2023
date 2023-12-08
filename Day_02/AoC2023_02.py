test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''.splitlines()

with open('input.txt', 'r') as f:
    games_log = f.readlines()

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# Part 1

valid_games = []

for line in games_log:
    gameID, games = line.strip().split(':')
    gameID = int(gameID.split()[1])
    games = games.split(';')
    valid = True
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            count, color = cube.split()
            count = int(count)
            if count > max_cubes[color]:
                valid = False
                break
    if valid:
        valid_games.append(gameID)

print(f'The sum of the IDs of valid games is {sum(valid_games)}.')

# Part 2

power_sum = 0

for line in games_log:
    gameID, games = line.strip().split(':')
    gameID = int(gameID.split()[1])
    games = games.split(';')
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            count, color = cube.split()
            count = int(count)
            if count > mins[color]:
                mins[color] = count
    power = mins['red'] * mins['green'] * mins['blue']
    power_sum += power

print(f'The sum of the power of game sets is {power_sum}.')
#%%
