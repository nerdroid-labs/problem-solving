from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
nums = deque([i for i in range(1, N + 1)])
stack = deque()
seq = []

for n in range(N):
    seq.append(int(input()))

i = 0
out = []
while i < N:
    if stack and seq[i] == stack[-1]:
        stack.pop()
        out.append("-")
        i += 1

    elif nums:
        stack.append(nums.popleft())
        out.append("+")

    else: break

if i != N: print("NO")
else: print(*out, sep="\n")