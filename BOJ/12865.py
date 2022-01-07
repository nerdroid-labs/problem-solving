import sys


def input():
	return sys.stdin.readline().rstrip()


N, K = list(map(int, input().split()))
item = []

for _ in range(N):
	item.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N)]

for n in range(N):
	w, visit_matrix = item[n]

	for k in range(K + 1):
		if w > k:
			dp[n][k] = dp[n-1][k]
		else:
			dp[n][k] = max(dp[n-1][k], dp[n-1][k - w] + visit_matrix)

print(dp[-1][-1])
