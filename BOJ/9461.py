import sys
input = sys.stdin.readline

dp = [-1 for i in range(100 + 1)]
dp[1] = 1
dp[2] = 1
dp[3] = 1


def get_P(n):
    global dp

    if dp[n] == -1: dp[n] = get_P(n-2) + get_P(n-3)
    return dp[n]

for _ in range(int(input())):
    N = int(input())
    print(get_P(N))
