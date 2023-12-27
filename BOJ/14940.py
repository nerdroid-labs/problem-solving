import sys
import collections


def input() -> str:
    return sys.stdin.readline().strip()


N, M = list(map(int, input().split()))
graph = []

visited = [[False] * M for _ in range(N)]
answer = [[0] * M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().split())))

start_m, start_n = -1, -1
for n in range(N):
    for m in range(M):
        if graph[n][m] == 2:
            start_m, start_n = m, n

queue = collections.deque()
queue.append((start_m, start_n, 0))
while queue:
    x, y, w = queue.popleft()

    if visited[y][x]:
        continue

    visited[y][x] = True
    answer[y][x] = w

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] != 0 and not visited[ny][nx]:
            queue.append((nx, ny, answer[y][x] + 1))

for n in range(N):
    for m in range(M):
        if not visited[n][m] and graph[n][m] != 0:
            answer[n][m] = -1

for line in answer:
    print(*line, sep=" ")
