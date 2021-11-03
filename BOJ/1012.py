import collections
import sys
input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

for t in range(int(input())):
    M, N, K = list(map(int, input().split()))
    coords = []
    deque = collections.deque()
    graph = [[0] * M for n in range(N)]
    visited = [[None] * M for n in range(N)]
    connected_components = 0

    for k in range(K):
        x, y = list(map(int, input().split()))
        graph[y][x] = 1
        visited[y][x] = False
        coords.append((y, x))

    for y, x in coords:
        if not visited[y][x]:
            connected_components += 1
            deque.append((y, x))

            while deque:
                y, x = deque.pop()
                visited[y][x] = True

                for i in range(4):
                    next_x = x + dx[i]
                    next_y = y + dy[i]
                    next_coord = [next_y, next_x]

                    if next_x in range(M) and next_y in range(N) and \
                            graph[next_y][next_x] == 1 and visited[next_y][next_x] not in (True, None):
                        deque.append(next_coord)

    print(connected_components)
