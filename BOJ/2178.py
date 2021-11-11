import sys
import collections
input = sys.stdin.readline

N, M = list(map(int, input().split()))
mat = []
visit = [[False] * M for _ in range(N)]
diff = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    mat.append([int(i) for i in input().rstrip()])

r, c, dist = 0, 0, 1
queue = collections.deque()
queue.appendleft((r, c, dist))

while queue:
    r, c, dist = queue.popleft()
    if visit[r][c]: continue
    else: visit[r][c] = True

    if r == N - 1 and c == M - 1:
        print(dist)

    for dy, dx in diff:
        if r + dy in range(N) and c + dx in range(M) and mat[r + dy][c + dx] == 1:
            queue.append((r + dy, c + dx, dist + 1))
