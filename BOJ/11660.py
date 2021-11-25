import sys
def input(): return sys.stdin.readline().rstrip()

matrix = []
N, M = list(map(int, input().split()))

for _ in range(N):
    matrix.append(list(map(int, input().split())))

for r in range(N):
    for c in range(1, N):
        matrix[r][c] = matrix[r][c] + matrix[r][c - 1]

for _ in range(M):
    r1, c1, r2, c2 = list(map(lambda x: int(x) - 1, input().split()))
    ret = 0

    for r in range(r1, r2 + 1):
        ret += matrix[r][c2]
        if c1 > 0:
            ret -= matrix[r][c1 - 1]

    print(ret)
    