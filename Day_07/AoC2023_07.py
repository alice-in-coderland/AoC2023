import numpy as np

allcards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1] #Part 1
alltypes = ['Five of a kind', 'Four of a kind', 'Full house', 'Three of a kind', 'Two pair', 'One pair', 'High card'][::-1]

test_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''.splitlines()

with open('input.txt', 'r') as f:
    camel_cards = f.read().splitlines()


# inp = test_input
inp = camel_cards

# Part 1
class Hand:
    def __init__(self, handcards, bid):
        self.handcards = handcards
        self.bid = int(bid)
        self.hand_type = self.get_hand_type()
        self.rank = np.NaN

    def __repr__(self):
        return f'Hand: {self.handcards}\tbid: {self.bid}\ttype: {self.hand_type}\trank: {self.rank}'

    def get_hand_type(self):
        handelems = [self.handcards.count(card) for card in allcards]
        if max(handelems) == 5:
            return alltypes[6]
        elif max(handelems) == 4:
            return alltypes[5]
        elif max(handelems) == 3:
            if 2 in handelems:
                return alltypes[4]
            else:
                return alltypes[3]
        elif max(handelems) == 2:
            if handelems.count(2) == 2:
                return alltypes[2]
            else:
                return alltypes[1]
        else:
            return alltypes[0]

    def __gt__(self, other):
        if alltypes.index(self.hand_type) > alltypes.index(other.hand_type):
            return True
        elif self.hand_type == other.hand_type:
            i = 0
            while i < len(self.handcards):
                if allcards.index(self.handcards[i]) == allcards.index(other.handcards[i]):
                    i += 1
                    continue
                elif allcards.index(self.handcards[i]) > allcards.index(other.handcards[i]):
                    return True
                else:
                    return False
        else:
            return False

    def __lt__(self, other):
        if alltypes.index(self.hand_type) < alltypes.index(other.hand_type):
            return True
        elif self.hand_type == other.hand_type:
            i = 0
            while i < len(self.handcards):
                if allcards.index(self.handcards[i]) == allcards.index(other.handcards[i]):
                    i += 1
                    continue
                elif allcards.index(self.handcards[i]) < allcards.index(other.handcards[i]):
                    return True
                else:
                    return False
        else:
            return False

    def __eq__(self, other):
        if self.hand_type == other.hand_type:
            if self.handcards == other.handcards:
                return True

    def set_rank(self, rank):
        self.rank = rank

    def calculate_winnings(self):
        return self.bid * self.rank


hands = []
for i, line in enumerate(inp):
    cards, bid = line.split()
    hands.append(Hand(cards, bid))

# print()

total_winnings = 0
for i, hand in enumerate((sorted(hands))):
    hand.set_rank(i+1)
    total_winnings += hand.calculate_winnings()

print(f'Total winnings: {total_winnings}.')


# Part 2

allcards_pt2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1] #Part 2


class HandTwo:
    def __init__(self, handcards, bid):
        self.handcards = handcards
        self.bid = int(bid)
        self.hand_type = self.get_hand_type()
        self.rank = np.NaN

    def __repr__(self):
        return f'Hand: {self.handcards}\tbid: {self.bid}\ttype: {self.hand_type}\trank: {self.rank}'

    def get_hand_type(self):
        handelems = [self.handcards.count(card) for card in allcards_pt2 if card != 'J']
        Js = self.handcards.count('J')
        if max(handelems) == 5:
            return alltypes[6]
        elif max(handelems) == 4:
            if Js == 1:
                return alltypes[6]
            else:
                return alltypes[5]
        elif max(handelems) == 3:
            if Js == 1:
                return alltypes[5]
            elif Js == 2:
                return alltypes[6]
            elif 2 in handelems:
                return alltypes[4]
            else:
                return alltypes[3]
        elif max(handelems) == 2:
            if handelems.count(2) == 2:
                if Js == 1:
                    return alltypes[4]
                else:
                    return alltypes[2]
            elif Js == 1:
                return alltypes[3]
            elif Js == 2:
                return alltypes[5]
            elif Js == 3:
                return alltypes[6]
            else:
                return alltypes[1]
        else:
            if Js == 1:
                return alltypes[1]
            elif Js == 2:
                return alltypes[3]
            elif Js == 3:
                return alltypes[5]
            elif Js == 4:
                return alltypes[6]
            elif Js == 5:
                return alltypes[6]
            else:
                return alltypes[0]

    def __gt__(self, other):
        if alltypes.index(self.hand_type) > alltypes.index(other.hand_type):
            return True
        elif self.hand_type == other.hand_type:
            i = 0
            while i < len(self.handcards):
                if allcards_pt2.index(self.handcards[i]) == allcards_pt2.index(other.handcards[i]):
                    i += 1
                    continue
                elif allcards_pt2.index(self.handcards[i]) > allcards_pt2.index(other.handcards[i]):
                    return True
                else:
                    return False
        else:
            return False

    def __lt__(self, other):
        if alltypes.index(self.hand_type) < alltypes.index(other.hand_type):
            return True
        elif self.hand_type == other.hand_type:
            i = 0
            while i < len(self.handcards):
                if allcards_pt2.index(self.handcards[i]) == allcards_pt2.index(other.handcards[i]):
                    i += 1
                    continue
                elif allcards_pt2.index(self.handcards[i]) < allcards_pt2.index(other.handcards[i]):
                    return True
                else:
                    return False
        else:
            return False

    def __eq__(self, other):
        if self.hand_type == other.hand_type:
            if self.handcards == other.handcards:
                return True

    def set_rank(self, rank):
        self.rank = rank

    def calculate_winnings(self):
        return self.bid * self.rank


hands_two = []
for i, line in enumerate(inp):
    cards, bid = line.split()
    hands_two.append(HandTwo(cards, bid))


total_winnings = 0
for i, hand in enumerate((sorted(hands_two))):
    hand.set_rank(i+1)
    total_winnings += hand.calculate_winnings()
    # print(hand)

print(f'Total winnings: {total_winnings}.')
# %%
