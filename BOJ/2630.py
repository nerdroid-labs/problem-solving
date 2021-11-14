import sys
input = sys.stdin.readline


def same_element(arr):
    element = arr[0][0]
    same = True

    for row in arr:
        for col in row:
            if col != element:
                same = False
                break

    return same, element


def recursive(arr):
    global ctr
    same, element = same_element(arr)

    if same: ctr[element] += 1
    else:
        size = len(arr) // 2

        for r_s, r_e in [(size * i, size * (i + 1)) for i in range(2)]:
            for c_s, c_e in [(size * i, size * (i + 1)) for i in range(2)]:
                sep_arr = [row[c_s:c_e] for row in arr[r_s:r_e]]
                recursive(sep_arr)


N = int(input())
matrix = []
ctr = [0, 0]

for _ in range(N):
    matrix.append(list(map(int, input().split())))

recursive(matrix)
print(*ctr, sep="\n")
