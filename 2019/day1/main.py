def fuel(m):
    import math
    return (math.floor(m / 3) - 2)


def recursive_fuel(m):
    if (m <= 0):
        return 0

    curr = max(fuel(m), 0)
    # print(m, curr)

    return (curr + recursive_fuel(curr))


# print(recursive_fuel(1969))  # should be 966


def solve(lines):
    # find total fuel required
    # fuel required for a module := mass / 3, round down, and subtract 2.
    summed = sum(
        (recursive_fuel(int(m)))
        for m in lines)
    print(summed)
