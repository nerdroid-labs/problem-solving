# https://t-anb.tistory.com/10
import sys


def input():
	return sys.stdin.readline().rstrip()


def get_i_to_j(i, j):
	global dp, mat

	if dp[i][j] is not None:
		return dp[i][j]
	elif i == j:
		dp[i][j] = 0
		return dp[i][j]
	elif i == j - 1:
		dp[i][j] = mat[i][0] * mat[i][1] * mat[j][1]
		return dp[i][j]
	else:
		dp[i][j] = sys.maxsize
		for s in range(i, j):
			dp[i][j] = min(dp[i][j], get_i_to_j(i, s) + get_i_to_j(s + 1, j) + mat[i][0] * mat[s][1] * mat[j][1])

		return dp[i][j]


N = int(input())
mat = []
dp = [[None] * N for _ in range(N)]

for i in range(N):
	mat.append(list(map(int, input().split())))

print(get_i_to_j(0, N - 1))
