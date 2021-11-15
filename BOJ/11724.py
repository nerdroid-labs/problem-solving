import sys
import collections
input = sys.stdin.readline

N, M = list(map(int, input().split()))
visited = [False for _ in range(N + 1)]
graph = collections.defaultdict(list)

for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

visit_ctr = 0
comp_ctr = 0
while visit_ctr < N:
    comp_ctr += 1
    queue = collections.deque()
    for i in range(1, N + 1):
        if not visited[i]:
            queue.append(i)
            break

    while queue:
        node = queue.popleft()
        if visited[node]: continue
        else:
            visited[node] = True
            visit_ctr += 1

        for adj in graph[node]:
            if not visited[adj]:
                queue.append(adj)

print(comp_ctr)
