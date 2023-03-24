import time
from util import numbers
import multiprocessing


def cpu_bound(n):
    return sum(i * i for i in range(n))


def find_sums(nums):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, nums)


# duration : 36.48695683479309
if __name__ == "__main__":
    st = time.time()
    find_sums(numbers)
    et = time.time()
    duration = (et - st)
    print(f"duration : {duration}")
