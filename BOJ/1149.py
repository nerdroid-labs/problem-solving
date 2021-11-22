import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
matrix = []
answer = float('inf')

for _ in range(N):
    matrix.append(list(map(int, input().split())))

# dp[x][c] : x번째에서 C를 골랐을때 최소값
dp = [[float('inf')] * 3 for _ in range(N)]
for c in range(3):
    dp[0][c] = matrix[0][c]

for x in range(1, N):
    for c in range(3):
        for except_c in range(3):
            if c == except_c: continue
            dp[x][c] = min(dp[x][c], matrix[x][c] + dp[x-1][except_c])

print(min(dp[-1]))
