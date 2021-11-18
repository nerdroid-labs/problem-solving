import collections
import sys
input = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

for t in range(int(input())):
    M, N, K = list(map(int, input().split()))
    graph = [[0] * M for n in range(N)]
    visited = [[False] * M for n in range(N)]
    connected_components = 0

    for k in range(K):
        x, y = list(map(int, input().split()))
        graph[y][x] = 1


    def dfs(r, c):
        visited[r][c] = True

        if not graph[r][c]: return False
        else:
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    dfs(nr, nc)

            return True


    for r in range(N):
        for c in range(M):
            if not visited[r][c] and dfs(r, c):
                connected_components += 1

    print(connected_components)
