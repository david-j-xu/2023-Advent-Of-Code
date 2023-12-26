def solve_line(sequence, numbers):
    memo = {}

    def memoize(numbers, idx, result):
        memo[(numbers, idx)] = result
        return result

    def helper(numbers, idx):
        if (numbers, idx) in memo:
            return memo[(numbers, idx)]

        def next_helper_if_period():
            return helper(numbers, idx + 1)

        def next_helper_if_hash():
            cand_sequence = sequence[idx:idx + numbers[0]]
            if (
                # sequence ends before # sequence can be completed
                len(cand_sequence) != numbers[0] or
                # there's a period somewhere in the sequence
                not all([x in "?#" for x in cand_sequence]) or
                # the next thing is not a period or the end of the sequence
                (idx + numbers[0] < len(sequence)
                 and sequence[idx + numbers[0]] not in '.?')
            ):
                return 0
            else:
                return helper(numbers[1:], idx + numbers[0] + 1)

        # if numbers is empty, we are done. check sequence has no more #
        if not numbers:
            result = 0
            if idx >= len(sequence) or not any([char == "#" for char in sequence[idx:]]):
                result = 1
            return memoize(numbers, idx, result)

        if idx >= len(sequence):
            # still have stuff left to do but no sequence left. this is invalid
            return memoize(numbers, idx, 0)

        if sequence[idx] == ".":
            return memoize(numbers, idx, next_helper_if_period())
        elif sequence[idx] == "#":
            return memoize(numbers, idx, next_helper_if_hash())
        else:
            return memoize(numbers, idx, next_helper_if_period() +
                           next_helper_if_hash())

    return helper(numbers, 0)


with open("input") as f:
    lines = [line[:-1].split(" ") for line in f.readlines()]
    lines = [([c for c in seq],
             tuple([int(number) for number in numbers.split(",")]))
             for seq, numbers in lines]
    lines = [(4 * (seq + ['?']) + seq, numbers * 5) for seq, numbers in lines]
    print(sum([solve_line(*line) for line in lines]))
