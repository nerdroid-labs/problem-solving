import sys
input = sys.stdin.readline

def fibo(n):
    global dp

    if dp[n] != [-1, -1]:
        return dp[n]
    else:
        left_0, left_1 = fibo(n-1)
        right_0, right_1 = fibo(n-2)
        dp[n] = [left_0 + right_0, left_1 + right_1]
        return dp[n]

#dp[n] = [#0, #1]
dp = [[-1, -1] for i in range(40 + 1)]
dp[0] = [1, 0]
dp[1] = [0, 1]
dp[2] = [1, 1]

for t in range(int(input())):
    N = int(input())
    zero, one = fibo(N)
    print(zero, one)
