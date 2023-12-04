def tokenize(line):
    digits = []

    digits_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    def tokenize_helper(line):
        if not line:
            return
        if line[0] in "123456789":
            digits.append(int(line[0]))
            tokenize_helper(line[1:])
            return
        else:
            for d_str, d_val in digits_map.items():
                if line.startswith(d_str):
                    digits.append(d_val)
                    # apparently eightwo is [8, 2] and not [8]. bruh.
                    tokenize_helper(line[1:])
                    return
            tokenize_helper(line[1:])

    tokenize_helper(line)

    return digits


with open("input") as f:
    lines = f.readlines()
    nums = [tokenize(line) for line in lines]

    print(sum(10 * num[0] + num[-1] for num in nums))
