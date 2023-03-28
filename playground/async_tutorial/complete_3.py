import asyncio
import itertools as it
import os
import time
import random
import argparse

# Async QUEUE (producers ~ consumers)


def makeitem(size: int = 5):
    return os.urandom(size).hex()


async def randsleep(caller=None):
    i = random.randint(0, 10)
    if (caller is not None):
        print(f"caller {caller} sleeping for {i} seconds")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue):
    n = random.randint(0, 10)
    # synchronous loop for each producer (put N items in Q)
    for _ in it.repeat(None, n):
        await randsleep(caller=f"Producer {name}")
        i = makeitem()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"Producer {name} put item {name} on queue")


async def consume(name: int, q: asyncio.Queue):
    # Loop : Keep consuming until done
    while True:
        await randsleep(f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"Consumer {name} got elem {i} in {now-t:0.5f} seconds")
        # marks popped Q elem as "done"
        q.task_done()


async def main(nprod: int, ncon: int):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]
    await asyncio.gather(*producers)
    # join() blocks (exec hangs) UNTIL 0 remaining unfinished taskss
    # each task completed by CONSUMER by calling task_done()
    await q.join()  # awaits producers + (implicitly) waits consumers
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=2)
    parser.add_argument("-c", "--ncon", type=int, default=5)
    ns = parser.parse_args()
    st = time.perf_counter()
    asyncio.run(main(**ns.__dict__))
    et = time.perf_counter()
    print(f"Program completed in {et-st:0.5f} seconds")
