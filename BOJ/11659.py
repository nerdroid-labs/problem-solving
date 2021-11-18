import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
nums = list(map(int, input().rstrip().split()))
totals = [nums[0]]

for i in range(1, N):
    totals.append(totals[-1] + nums[i])

for _ in range(M):
    s, e = list(map(lambda x: int(x) - 1, input().rstrip().split()))

    if s > 0: print(totals[e] - totals[s-1])
    else: print(totals[e])
