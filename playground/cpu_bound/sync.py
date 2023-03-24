import time
from util import numbers


def cpu_bound(num):
    return sum(i * i for i in range(num))


def find_sums(nums):
    for n in nums:
        print(n)
        cpu_bound(n)


# duration : 263.7033431529999
if __name__ == "__main__":
    st = time.time()
    find_sums(numbers)
    et = time.time()
    duration = (et - st)
    print(f"duration : {duration}")
