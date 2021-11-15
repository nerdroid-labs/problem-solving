def get_case(n):
    global dp
    if dp[n] != -1:
        return dp[n]

    if n == 0:
        ret = 1
    elif n == 1:
        ret = 1
    else:
        ret = get_case(n - 1) + get_case(n - 2)

    dp[n] = ret
    return ret

n = int(input())
dp = [-1 for _ in range(1000 + 1)]
print(get_case(n) % 10007)
