import collections
import sys

input = sys.stdin.readline

queue = collections.deque()
N = int(input())
for n in range(N):
    line = input()
    if "push" in line:
        queue.append(int(line.split()[1]))
    elif "front" in line:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif "back" in line:
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif "size" in line:
        print(len(queue))
    elif "empty" in line:
        if queue:
            print(0)
        else:
            print(1)
    elif "pop" in line:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
