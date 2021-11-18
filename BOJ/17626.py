import sys
input = sys.stdin.readline

N = int(input())

dp = [float('inf') for _ in range(N + 1)]
dp[0] = 0
dp[1] = 1

for n in range(2, N + 1):
    for root in range(1, int(n ** 0.5) + 1):
        dp[n] = min(dp[n], dp[n - root ** 2] + 1)

print(dp[N])
