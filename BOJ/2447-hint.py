def getStars(N, mat, x, y):
    if N == 3:
        for i in range(N):
            for j in range(N):
                if i == 1 and j == 1:
                    mat[x+i][y+j]=" "
                else:
                    mat[x+i][y+j]="*"

    else:
        for i in range(3):
            for j in range(3):
                getStars(N//3, mat, x + i * N // 3, y + j * N // 3)

                if i == 1 and j == 1:
                    for s in range(N//3):
                        for t in range(N//3):
                            mat[x + i * N // 3 + s][y + j * N // 3 + t] = " "


N = int(input())
mat = [["" for j in range(N) ] for i in range(N)]
getStars(N, mat, 0, 0)

for matrix in mat:
    print("".join(matrix))