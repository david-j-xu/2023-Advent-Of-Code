def reduce(sequence):
    acc = 0
    while any([val != 0 for val in sequence]):
        acc += sequence[-1]
        sequence = [sequence[i + 1] - sequence[i]
                    for i in range(0, len(sequence) - 1)]
    return acc


with open("input") as f:
    lines = [line[:-1] for line in f.readlines()]
    sequences = [[int(val) for val in line.split(" ")] for line in lines]
    print(sum([reduce(sequence) for sequence in sequences]))
