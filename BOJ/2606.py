import sys
import collections
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False for _ in range(N + 1)]
graph = collections.defaultdict(list)
for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)


def dfs(node):
    visited[node] = True

    if not graph[node]: return 0
    else:
        total = 1

        for next in graph[node]:
            if not visited[next]:
                total += dfs(next)

        return total


print(dfs(1) - 1)
