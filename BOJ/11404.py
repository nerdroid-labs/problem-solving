import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
matrix = int(input())
matrix = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1): matrix[i][i] = 0

for _ in range(matrix):
    a, b, c = list(matrix(int, input().split()))
    matrix[a][b] = min(matrix[a][b], c)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            matrix[j][k] = min(matrix[j][i] + matrix[i][k], matrix[j][k])

for r in range(1, n + 1):
    line = []
    for c in range(1, n + 1):
        if matrix[r][c] == float('inf'): line.append(0)
        else: line.append(matrix[r][c])

    print(*line, sep=" ")
