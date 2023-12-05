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
    cards = [len(set(winners) & set(nums)) for _, winners, nums in cards]
    print(sum([2 ** (i - 1) for i in cards if i > 0]))
