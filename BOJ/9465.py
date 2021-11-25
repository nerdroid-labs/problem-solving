import sys
def input(): return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[-1] * N for _ in range(2)]
    matrix = []
    for _ in range(2): matrix.append(list(map(int, input().split())))

    if N == 1:
        print(max(matrix[0][0], matrix[1][0]))
    elif N == 2:
        print(max(matrix[0][0] + matrix[1][1], matrix[1][0] + matrix[0][1]))
    else:
        dp[0][0] = matrix[0][0]
        dp[1][0] = matrix[1][0]
        dp[0][1] = dp[1][0] + matrix[0][1]
        dp[1][1] = dp[0][0] + matrix[1][1]

        for c in range(2, N):
            dp[0][c] = max(dp[1][c - 2], dp[1][c - 1]) + matrix[0][c]
            dp[1][c] = max(dp[0][c - 2], dp[0][c - 1]) + matrix[1][c]

        print(max(max(dp[0]), max(dp[1])))
