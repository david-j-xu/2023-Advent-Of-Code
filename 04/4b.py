with open("input") as f:
    cards = f.readlines()

    def parse_line(line):
        id, rest = line[:-1].split(": ")
        winners, nums = rest.split(" | ")
        id = id[5:]
        winners = [int(winner) for winner in winners.split(" ") if winner]
        nums = [int(num) for num in nums.split(" ") if num]

        return (id, winners, nums)

    cards = [parse_line(line) for line in cards]
    winners = [len(set(winners) & set(nums)) for _, winners, nums in cards]
    num_cards = [1 for _ in cards]

    for i, num_winners in enumerate(winners):
        for j in range(i + 1, min(len(num_cards), i + num_winners + 1)):
            num_cards[j] += num_cards[i]
    print(sum(num_cards))
