import sys


def input():
	return sys.stdin.readline().rstrip()


N, K = list(map(int, input().split()))
dp = [0] * (K + 1)
for n in range(N):
	weight, value = list(map(int, input().split()))
	for w in reversed(range(1, K + 1)):
		if weight <= w:
			dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[-1])
