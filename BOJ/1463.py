import sys
import collections
import time
input = sys.stdin.readline

N = int(input())
# st = time.time()

dp = dict()
queue = collections.deque()
queue.append((N, 0))

while True:
    if not queue: break
    X, ctr = queue.popleft()

    if X in dp:
        if dp[X] < ctr: continue
        dp[X] = min(dp[X], ctr)
    else:
        dp[X] = ctr

    if X == 1:
        break

    if X % 3 == 0:
        queue.append((X // 3, ctr + 1))

    if X % 2 == 0:
        queue.append((X // 2, ctr + 1))

    queue.append((X - 1, ctr + 1))

# et = time.time()
print(dp[1])
