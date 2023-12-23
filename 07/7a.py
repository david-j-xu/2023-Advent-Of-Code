card_mappings = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,
                 '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


class Hand:
    def __init__(self, one, two, three, four, five) -> None:
        self.cards = (one, two, three, four, five)
        self.counts = {}
        for i in self.cards:
            if i in self.counts:
                self.counts[i] += 1
            else:
                self.counts[i] = 1
        self.classify()

    def of_string(string):
        return Hand(*[card_mappings[i] for i in string])

    def classify(self):
        max_count = max(self.counts.values())
        if max_count == 5:
            self.power = 7
        elif max_count == 4:
            self.power = 6
        elif max_count == 3:
            if min(self.counts.values()) == 2:
                self.power = 5
            else:
                self.power = 4
        elif max_count == 2:
            if len([pair for pair in self.counts.values() if pair == 2]) == 2:
                self.power = 3
            else:
                self.power = 2
        else:
            self.power = 1

    def __lt__(self, other):
        if other.power > self.power:
            return True
        elif other.power == self.power and other.cards > self.cards:
            return True

        return False

    def __eq__(self, __value: object) -> bool:
        return __value.power == self.power and __value.cards == self.cards

    def __repr__(self) -> str:
        return f"({self.cards}, {self.power})"


with open("input") as f:
    hands = [line[:-1].split(" ") for line in f.readlines()]
    hands = [(Hand.of_string(hand), int(bid)) for hand, bid in hands]
    ranked_hands = zip(range(1, len(hands) + 1),
                       [hand[1] for hand in sorted(hands)])

    print(sum([a * b for a, b in ranked_hands]))
