import sys


def input():
	return sys.stdin.readline().rstrip()


def check(s, e):
	global nums, dp
	if dp[s][e]:
		return dp[s][e]

	if nums[s] == nums[e]:
		if 0 <= s + 1 <= e - 1 < N:
			dp[s][e] = check(s + 1, e - 1)
		else:
			dp[s][e] = 1
	else:
		dp[s][e] = 0

	return dp[s][e]


N = int(input())
nums = list(map(int, input().split()))
M = int(input())
dp = [[None] * N for _ in range(N)]

for e in range(N):
	for s in range(e + 1):
		check(s, e)

for i in range(M):
	s, e = list(map(lambda x: int(x) - 1, input().split()))
	print(dp[s][e])

