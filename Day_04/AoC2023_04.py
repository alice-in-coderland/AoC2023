test_input = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''.splitlines()

with open('input.txt', 'r') as f:
    scratchcards = f.readlines()

inp = test_input


class scratchcard:
    def __init__(self, cardno, win, have):
        self.no = cardno
        self.winning = win
        self.having = have

    def get_score(self):
        score = 0
        for i in self.winning:
            if i in self.having:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        return score

    def get_matching(self):
        return len([i for i in self.winning if i in self.having])

# Part 1


pile_score = 0

for line in scratchcards:
    parseline = line.split(':')
    win = [int(x) for x in parseline[1].split('|')[0].split()]
    have = [int(x) for x in parseline[1].split('|')[1].split()]
    card = scratchcard(int(parseline[0].split()[1]), win, have)
    pile_score += card.get_score()

print(f'The scratch cards are worth {pile_score} points in total.')


# Part 2


scratch_dict = {}

for line in test_input:
    parseline = line.split(':')
    win = [int(x) for x in parseline[1].split('|')[0].split()]
    have = [int(x) for x in parseline[1].split('|')[1].split()]
    card = scratchcard(int(parseline[0].split()[1]), win, have)
    scratch_dict[card.no] = [1, card.get_matching()]


def win_more_cards():
    for scratchcard in scratch_dict:
        for i in range(scratch_dict[scratchcard][0]):
            scratch_dict[scratchcard][0]


