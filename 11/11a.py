from itertools import combinations
with open("input") as f:
    rows = [list(map(lambda x: x == "#", line[:-1]))
            for line in f.readlines()]

    empty_rows = [idx for idx, row in enumerate(rows) if not any(row)]
    empty_cols = [idx for idx, col in enumerate(zip(*rows)) if not any(col)]

    galaxies = [(r, c) for r, row in enumerate(rows)
                for c, value in enumerate(row) if value]

    galaxies = [(r + len(list(filter(lambda x: x < r, empty_rows))), c +
                 len(list(filter(lambda x: x < c, empty_cols)))) for r, c in galaxies]

    sum = 0
    for (r1, c1), (r2, c2) in combinations(galaxies, 2):
        sum += max(c1, c2) - min(c1, c2) + max(r1, r2) - min(r1, r2)

    print(sum)
