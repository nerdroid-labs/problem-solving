import collections
import sys
input = sys.stdin.readline

stack = collections.deque()
N = int(input())
for n in range(N):
    line = input()
    if "push" in line:
        stack.append(int(line.split()[1]))
    elif "top" in line:
        if stack: print(stack[-1])
        else: print(-1)
    elif "size" in line:
        print(len(stack))
    elif "empty" in line:
        if stack: print(0)
        else: print(1)
    elif "pop" in line:
        if stack: print(stack.pop())
        else: print(-1)
        