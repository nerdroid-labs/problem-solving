import collections
import sys
import time

sys.setrecursionlimit(10 ** 4)
def input(): return sys.stdin.readline().rstrip()


MAX_VALUE = 100000
N, K = list(map(int, input().split()))
dp = dict()
queue = collections.deque()
queue.append((N, 0 ))

min_time = float('inf')
min_time_ctr = 0
while queue:
    X, ctr = queue.popleft()

    dp[X] = min(dp.get(X, float("inf")), ctr)
    if dp[X] < ctr: continue

    if X == K:
        if min_time == ctr:
            min_time_ctr += 1
        elif min_time > ctr:
            min_time = ctr
            min_time_ctr = 1
        continue

    if X * 2 <= MAX_VALUE * 1.5:
        queue.append((X * 2, ctr + 1))
    if X + 1 <= MAX_VALUE:
        queue.append((X + 1, ctr + 1))
    if X - 1 >= 0:
        queue.append((X - 1, ctr + 1))

print(min_time)
print(min_time_ctr)
