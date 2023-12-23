import math


def find_num_solutions(time, dist):
    # quadratic formula heheheh
    if time ** 2 - 4 * dist <= 0:
        # if imaginary solutions or only one zero (on the axis), return 0
        return 0
    radical = math.sqrt(time ** 2 - 4 * dist)
    solns = math.ceil((time - radical) / 2), math.floor((time + radical) / 2)

    if math.floor(radical) == radical:
        # we are at the zeros, need to move the solutions by one
        solns = solns[0] + 1, solns[1] - 1

    return solns[1] - solns[0] + 1


with open("input") as f:
    lines = [line[:-1] for line in f.readlines()]
    time = int("".join(lines[0].split()[1:]))
    dist = int("".join(lines[1].split()[1:]))
    print(find_num_solutions(time, dist))
