
with open("input") as f:
    lines = [line[:-1] for line in f.readlines()]
    gears_mask = [[c == "*" for c in line] for line in lines]
    gears_adjacent_mask = [[[] for _ in line] for line in lines]

    gears = {}

    for r, row in enumerate(gears_adjacent_mask):
        for c, col in enumerate(row):
            if gears_mask[r][c]:
                gears[(r, c)] = []
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i >= 0 and i < len(gears_adjacent_mask) \
                                and j >= 0 and j < len(row):
                            gears_adjacent_mask[i][j].append((r, c))

    for r, line in enumerate(lines):
        curr = ""
        in_number = False
        adjacent_gears = set()

        for c, character in enumerate(line):
            if character in "1234567890":
                in_number = True
                curr += character
                adjacent_gears |= set(gears_adjacent_mask[r][c])
            else:
                if curr:
                    for gear in adjacent_gears:
                        gears[gear].append(int(curr))
                curr = ""
                adjacent_gears = set()
                in_number = False

        if curr and in_number:
            for gear in adjacent_gears:
                gears[gear].append(int(curr))

    print(sum([g[0] * g[1]
          for _, g in filter(lambda g: len(g[1]) == 2, gears.items())]))
