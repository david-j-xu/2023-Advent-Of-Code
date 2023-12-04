class Round:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Game:
    def __init__(self, id, rounds):
        self.id = id
        self.rounds = rounds

    def get_max_reds(self):
        return max([round.red for round in self.rounds])

    def get_max_greens(self):
        return max([round.green for round in self.rounds])

    def get_max_blues(self):
        return max([round.blue for round in self.rounds])


def parse_game(line: str):
    id, rounds_str = line.split(": ")
    id = int(id[5:])
    rounds = []
    rounds_str = [
        round.split(", ")
        for round in rounds_str.split("; ")
    ]

    for round in rounds_str:
        red, green, blue = (0, 0, 0)
        for entry in round:
            number, color = entry.split(" ")
            number = int(number)
            if color == "red":
                red = number
            elif color == "blue":
                blue = number
            elif color == "green":
                green = number

        rounds.append(Round(red, green, blue))

    return Game(id, rounds)


with open("input") as f:
    games = [parse_game(line[:-1]) for line in f.readlines()]

    valid_games = list(
        filter(
            lambda game: (
                (game.get_max_reds() <= 12) and
                (game.get_max_greens() <= 13) and
                (game.get_max_blues() <= 14)
            ),
            games
        )
    )

    print(sum([game.id for game in valid_games]))
