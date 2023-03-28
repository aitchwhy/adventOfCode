import asyncio
import random
import time

# CHAINING CO_ROUTINES (part1 -> part2)


async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds")
    await asyncio.sleep(i)
    result = f"result({n})-part1"
    print(f"Returning part1({n}) == {result} ")
    return result


async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2({n}, {arg}) sleeping for {i} seconds")
    await asyncio.sleep(i)
    result = f"result({n})-part2 derived from {arg}"
    print(f"Returning part2({n}, {arg}) == {result} ")
    return result


async def chain(n: int) -> None:
    st = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    et = time.perf_counter()
    print(f"---> Chained result(input {n}) => {p2} took {et-st:0.2f} seconds")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == "__main__":
    import sys
    random.seed(444)

    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start

    print(f"program ran in {end:.2f} seconds")
