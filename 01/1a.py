with open("input") as f:
    lines = f.readlines()
    nums = [list(filter(lambda x: x.isdigit(), line))
            for line in lines]
    nums = [int(val[0] + val[-1]) for val in nums]

    print(sum(nums))
