import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
div = 1000000007
dp = dict()
dp[0] = 0
dp[1] = 1


def fibo(n):
    if n in dp: return dp[n]
    else:
        if n % 2 == 0:
            k = n // 2
            ret = (2 * fibo(k - 1) + fibo(k)) * fibo(k)
        else:
            k = (n + 1) // 2
            ret = fibo(k) * fibo(k) + fibo(k - 1) * fibo(k - 1)

        dp[n] = ret % div
        return dp[n]


print(fibo(n))
