import sys
input = sys.stdin.readline


def check_same(matrix):
    num = matrix[0][0]
    same = True

    for row in matrix:
        for e in row:
            if e != num:
                same = False
                break

    return same, num


def recursive(matrix):
    global solution
    same, num = check_same(matrix)
    size = len(matrix)

    if same:
        solution[num + 1] += 1
        return

    else:
        next_size = size // 3

        for r in (i * next_size for i in range(3)):
            for c in (i * next_size for i in range(3)):
                next_mat = [row[c:c + next_size] for row in matrix[r:r + next_size]]
                recursive(next_mat)


solution = [0, 0, 0]
mat = []
for _ in range(int(input())):
    mat.append(list(map(int, input().split())))

recursive(mat)
print(*solution, sep="\n")
