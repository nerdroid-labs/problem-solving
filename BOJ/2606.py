import sys
import collections
input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False for _ in range(N+1)]
graph = collections.defaultdict(list)
for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

queue = collections.deque()
queue.appendleft(1)
ctr = -1

while queue:
    node = queue.popleft()
    if not visited[node]:
        visited[node] = True
        ctr += 1

        for adj in graph[node]:
            if not visited[adj]:
                queue.appendleft(adj)

print(ctr)