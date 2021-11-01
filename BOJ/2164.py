import collections

N = int(input())
deq = collections.deque(range(1, N+1))

while len(deq) > 1:
    deq.popleft()
    if len(deq) == 1: break

    deq.append(deq.popleft())

print(deq[0])