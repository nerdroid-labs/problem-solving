dp = [-1 for _ in range(1000 + 1)]


def case(n):
    global dp

    if dp[n] != -1: return dp[n]

    if n == 0:
        ret = 1
    elif n == 1:
        ret = 1
    else:
        ret = case(n - 2) * 2 + case(n - 1)

    dp[n] = ret
    return ret % 10007

print(case(int(input())))
