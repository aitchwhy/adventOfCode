import queue


def task(name, q):
    while not q.empty():
        count = q.get()
        total = 0
        print(f"Task {name} running")
        for x in range(count):
            total += 1
            yield
        print(f"Task {name} total: {total}")


def main():
    # main entry

    # Create Q of work
    work_queue = queue.Queue()

    # put work in Q
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # create workers to process Q
    tasks = [
        task("1", work_queue),
        task("2", work_queue),
    ]

    # run tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True


if __name__ == "__main__":
    main()
