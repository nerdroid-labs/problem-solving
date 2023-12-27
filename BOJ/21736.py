import collections
import sys


def input():
    return sys.stdin.readline().strip()


N, M = list(map(int, input().split()))
s_x, s_y = -1, -1
graph = []
for n in range(N):
    graph.append(input()[:])

for n in range(N):
    for m in range(M):
        if graph[n][m] == 'I':
            s_y, s_x = n, m

visited = [[False] * M for _ in range(N)]
deque = collections.deque()
answer = 0
visited[s_y][s_x] = True
deque.append((s_y, s_x))
while deque:
    r, c = deque.popleft()
    if graph[r][c] == 'P':
        answer += 1

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = c + dx, r + dy
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] != 'X':
            visited[ny][nx] = True
            deque.append((ny, nx))

print(answer if answer != 0 else 'TT')
