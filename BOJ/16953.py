import sys
sys.setrecursionlimit(10 ** 5)
def input(): return sys.stdin.readline().rstrip()


A, B = list(map(int, input().split()))
dp = dict()


def backtracking(A, n):
    if A > B or dp.get(A, float('inf')) < n: return
    else:
        dp[A] = min(dp.get(A, float('inf')), n)
        if A == B:
            return
        else:
            backtracking(A * 2, n + 1)
            backtracking(A * 10 + 1, n + 1)

backtracking(A, 1)
print(dp.get(B, -1))
