import sys
input = sys.stdin.readline

N = int(input())
block = []
matrix = []
visit = [[False] * N for _ in range(N)]

for r in range(N):
    line = list(map(int, [c for c in input().rstrip()]))
    matrix.append(line)


def dfs(r, c):
    visit[r][c] = True

    if not matrix[r][c]: return 0
    else:
        total = 1
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= r + dr < N and 0 <= c + dc < N and not visit[r + dr][c + dc]:
                total += dfs(r + dr, c + dc)

        return total


for r in range(N):
    for c in range(N):
        if not visit[r][c]:
            ctr = dfs(r, c)
            if ctr > 0:
                block.append(ctr)

print(len(block))
print(*sorted(block), sep="\n")
