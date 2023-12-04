
with open("input") as f:
    lines = [line[:-1] for line in f.readlines()]
    symbols_mask = [[c not in "1234567890." for c in line] for line in lines]
    symbols_adjacent_mask = [[False for _ in line] for line in lines]

    for r, row in enumerate(symbols_adjacent_mask):
        for c, col in enumerate(row):
            if symbols_mask[r][c]:
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i >= 0 and i < len(symbols_adjacent_mask) \
                                and j >= 0 and j < len(row):
                            symbols_adjacent_mask[i][j] = True
    numbers = []
    for r, line in enumerate(lines):
        curr = ""
        in_number = False
        adjacent = False

        for c, character in enumerate(line):
            if character in "1234567890":
                in_number = True
                curr += character
                adjacent |= symbols_adjacent_mask[r][c]
            else:
                if curr and adjacent:
                    numbers.append(int(curr))
                curr = ""
                adjacent = False
                in_number = False

        if in_number and adjacent:
            numbers.append(int(curr))

    print(sum(numbers))
