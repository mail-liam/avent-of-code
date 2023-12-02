import re
from aocd import get_data, submit

data = get_data(day=2, year=2023)
# data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

COLOURS = ("red", "green", "blue")
powers = []

for row in data.splitlines():
    game_no, game_data = row.split(":")
    game_id = int(re.search("\d+", game_no)[0])
    minimums = {colour: 0 for colour in COLOURS}
    
    for game in game_data.split(";"):
        for colour in COLOURS:
            re_match = re.search(f"(\d+) {colour}", game)
            total_shown = re_match[1] if re_match else 0

            minimums[colour] = max(int(total_shown), minimums[colour])

    power = 1
    for val in minimums.values():
        power *= val

    powers.append(power)


result = sum(powers)
print(result)
submit(result, part="b", day=2, year=2023)