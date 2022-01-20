import sys


def input():
	return sys.stdin.readline().rstrip()


def fibo(n):
	if dp[n] is None:
		dp[n] = fibo(n - 1) + fibo(n - 2)

	return dp[n]


N = int(input())
dp = [None] * (N + 1)
dp[0] = 0
dp[1] = 1

print(fibo(N))
