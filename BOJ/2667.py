import sys
import collections
input = sys.stdin.readline

N = int(input())
visited = [[False] * N for _ in range(N)]
matrix = []
coords = []

for r in range(N):
    line = list(map(int, [c for c in input().rstrip()]))
    matrix.append(line)

    for c in range(N):
        if matrix[r][c] == 1: coords.append((r, c))

block = []
while True:
    queue = collections.deque()
    house_num = 0

    found = False
    for r, c in coords:
        if not visited[r][c]:
            found = True
            queue.append((r, c))
            break

    if not found: break
    else:
        while queue:
            r, c = queue.popleft()
            if visited[r][c]: continue
            else:
                visited[r][c] = True
                house_num += 1

                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dy, c + dx
                    if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] and not visited[nr][nc]:
                        queue.append((nr, nc))

    block.append(house_num)

block.sort()
print(len(block))
print(*block, sep="\n")
