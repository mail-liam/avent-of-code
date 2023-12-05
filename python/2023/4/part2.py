import math
import re
from aocd import get_data, submit

data = get_data(day=4, year=2023)
# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


CARDS = []

def parse_numbers(numbers):
    res = []
    for n in numbers.split(" "):
        try:
            res.append(int(n))
        except ValueError:
            continue

    return res


class Card:
    def __init__(self, id, winning, numbers):
        self.id = id
        self.winning = winning
        self.numbers = numbers

    def get_score(self):
        score = 0
        for num in self.numbers:
            if num in self.winning:
                score += 1

        return score

for line in data.splitlines():
    card_no, cards = line.split(": ")
    card_number = int(re.search(f"\d+", card_no)[0])
    
    winning, entries = cards.split(" | ")

    winning_nums, entry_nums = parse_numbers(winning), parse_numbers(entries)

    CARDS.append(Card(card_number, winning_nums, entry_nums))

CARD_COUNTS = {card.id: 1 for card in CARDS}
MAX_COUNT = max(CARD_COUNTS)

for card in CARDS:
    # breakpoint()
    score = card.get_score()
    current_id = card.id
    count = CARD_COUNTS[current_id]

    for i in range(1, score + 1):
        next_card_id = current_id + i
        if next_card_id > MAX_COUNT:
            break
        CARD_COUNTS[next_card_id] += count

print(CARD_COUNTS)
result = sum(CARD_COUNTS.values())
print(result)
submit(result, part="b", day=4, year=2023)