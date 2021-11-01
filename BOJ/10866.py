import collections
import sys

input = sys.stdin.readline

deque = collections.deque()
N = int(input())
for n in range(N):
    line = input()
    if line.startswith("push_back"):
        deque.append(int(line.split()[1]))
    elif line.startswith("push_front"):
        deque.appendleft(int(line.split()[1]))
    elif line.startswith("pop_front"):
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif line.startswith("pop_back"):
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif line.startswith("front"):
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif line.startswith("back"):
        if deque:
            print(deque[-1])
        else:
            print(-1)
    elif line.startswith("size"):
        print(len(deque))
    elif line.startswith("empty"):
        if deque:
            print(0)
        else:
            print(1)
