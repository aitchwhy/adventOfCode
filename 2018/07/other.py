from collections import defaultdict
import fileinput
import re

# tasks is a set of all task names A - Z
tasks = set()
# deps maps tasks to a set of prerequisite tasks
deps = defaultdict(set)
for line in fileinput.input():
    a, b = re.findall(r' ([A-Z]) ', line)
    tasks |= {a, b}
    deps[b].add(a)

# part 1
done = []
for _ in tasks:
    # find the minimal (lexicographically) task that is not yet done
    # and has all of its prerequisites satisfied; add it to the list
    done.append(min(x for x in tasks if x not in done and deps[x] <= set(done)))
print(''.join(done))

# part 2
done = set()
seconds = 0      # total seconds elapsed
counts = [0] * 5 # seconds remaining for worker `i` to finish its current task
work = [''] * 5  # which task worker `i` is performing
while True:
    # decrement each workers remaining time
    # if a worker finishes, mark its task as completed
    for i, count in enumerate(counts):
        if count == 1:
            done.add(work[i])
        counts[i] = max(0, count - 1)
    # while there is an idle worker
    while 0 in counts:
        # find the idle worker
        i = counts.index(0)
        # find a task that has all of its prerequisites satisfied
        candidates = [x for x in tasks if deps[x] <= done]
        if not candidates:
            break
        task = min(candidates)
        tasks.remove(task)
        # have the worker start the selected task
        counts[i] = ord(task) - ord('A') + 61
        work[i] = task
    # if all workers are idle at this point, we are done
    if sum(counts) == 0:
        break
    seconds += 1
print(seconds)
