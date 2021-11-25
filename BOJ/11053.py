import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
nums = list(map(int, input().split()))
dp = [None] * N
answer = -1

dp[0] = [1, 0]
for i in range(1, N):
    best = [1, i]
    for j in range(i):
        length, last_idx = dp[j]
        if nums[last_idx] < nums[i]: best = max(best, [length + 1, i])
    dp[i] = best

print(max(dp)[0])
