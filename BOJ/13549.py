import sys
import collections
def input(): return sys.stdin.readline().rstrip()


N, K = list(map(int, input().split()))
dp = [float('inf')] * (200000 + 1)
queue = collections.deque()
queue.append((N, 0))

while queue:
    n, ctr = queue.popleft()
    dp[n] = min(dp[n], ctr)
    if dp[n] != ctr: continue

    if n == K:
        print(ctr)
        break

    if n * 2 <= 200000:
        queue.append((n * 2, ctr))
    if n - 1 >= 0:
        queue.append((n - 1, ctr + 1))
    if n + 1 <= 100000:
        queue.append((n + 1, ctr + 1))
