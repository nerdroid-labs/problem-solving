import collections

T = int(input())
for t in range(T):
    N, M = list(map(int, input().split()))

    queue = collections.deque()
    priorities = collections.deque()
    for i, p in enumerate(list(map(int, input().split()))):
        queue.append(i)
        priorities.append(p)

    idx = 0
    while priorities:
        current_index = queue[0]
        current_priority = priorities[current_index]

        max_priority = max([priorities[i] for i in queue])

        if max_priority > current_priority:
            queue.append(queue.popleft())

        else:
            i = queue.popleft()
            idx += 1

            if i == M:
                print(idx)
                break
