import sys
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
matrix = []
shape = (
    [[1, 1, 1, 1]],
    [[1], [1], [1], [1]],

    [[1, 1], [1, 1]],

    [[1, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [1, 1, 1]],
    [[0, 1], [1, 1], [0, 1]],
    [[1, 0], [1, 1], [1, 0]],

    [[1, 0], [1, 1], [0, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],

    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 1], [0, 1], [0, 1]],
    [[1, 1], [1, 0], [1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 1]]
)

for _ in range(N):
    matrix.append(list(map(int, input().split())))

# left-top
ans = float('-inf')
for r in range(N):
    for c in range(M):
        for s in shape:
            sub_ans = 0
            height, width = len(s), len(s[0])
            if r + height - 1 < N and c + width - 1 < M:
                for h in range(height):
                    for w in range(width):
                        sub_ans += matrix[r + h][c + w] * s[h][w]

            ans = max(ans, sub_ans)

print(ans)