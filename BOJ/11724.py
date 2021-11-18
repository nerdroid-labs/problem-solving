import sys
import collections
input = sys.stdin.readline

N, M = list(map(int, input().split()))
visited = [False for _ in range(N + 1)]
graph = collections.defaultdict(list)

for _ in range(M):
    s, e = list(map(int, input().rstrip().split()))
    graph[s].append(e)
    graph[e].append(s)


def dfs(node):
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(next)

connected_components = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        connected_components += 1


print(connected_components)
