import sys
input = sys.stdin.readline


def case(x):
    global dp
    if dp[x] != -1:
        return dp[x]

    if x == 1:
        # 1
        ret = 1
    elif x == 2:
        # 1 + 1, 2
        ret = 2
    elif x == 3:
        # 1 + 1 + 1, 1 + 2, 2 + 1, 3
        ret = 4
    else:
        ret = case(x-1) + case(x-2) + case(x-3)

    dp[x] = ret
    return ret


for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    dp = [-1 for i in range(11 + 1)]
    print(case(n))
