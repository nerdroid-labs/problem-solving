T = int(input())

mat = [[i for i in range(15)] for j in range(15)]

for r in range(1, 15):
    for c in range(1, 15):
        mat[r][c] = mat[r][c-1] + mat[r-1][c]

for t in range(T):
    k = int(input())
    n = int(input())
    print(mat[k][n])

