import sys
import collections
input = sys.stdin.readline

N, M = list(map(int, input().split()))
mat = []
visit = [[False] * M for _ in range(N)]
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N): mat.append(list(map(int, input().rstrip())))

queue = collections.deque()
queue.append((0, 0))

while queue:
    r, c = queue.popleft()
    if visit[r][c]: continue
    else: visit[r][c] = True

    for dy, dx in diff:
        if 0 <= r + dy < N and 0 <= c + dx < M and mat[r + dy][c + dx] == 1:
            queue.append((r + dy, c + dx))
            mat[r + dy][c + dx] = mat[r][c] + 1

print(mat[-1][-1])
