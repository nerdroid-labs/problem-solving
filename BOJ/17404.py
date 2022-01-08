import sys


def input():
	return sys.stdin.readline().rstrip()


# R, G, B
N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize

for start in range(3):
	dp = [[sys.maxsize] * 3 for _ in range(N)]
	dp[0][start] = costs[0][start]

	for i in range(1, N):
		for after in range(3):
			for before in range(3):
				if after == before or (i == N - 1 and after == start):
					continue

				dp[i][after] = min(dp[i][after], dp[i - 1][before] + costs[i][after])

	answer = min(min(dp[-1]), answer)

print(answer)
