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
        return str(num)

    else:
        gap = size // 2

        ret = ""
        for y, x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            r = y * gap
            c = x * gap

            next_mat = [row[c:c + gap] for row in matrix[r:r + gap]]
            ret += recursive(next_mat)

        return f"({ret})"


mat = []
for _ in range(int(input())):
    mat.append([int(i) for i in input().rstrip()])

print(recursive(mat))
