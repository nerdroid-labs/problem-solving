import collections
import sys
input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
graph = collections.defaultdict(list)

for m in range(M):
    s, t = list(map(int, input().split()))
    graph[s].append(t)
    graph[t].append(s)

stack = collections.deque()
visit = [False for i in range(N + 1)]

stack.append(V)
while stack:
    node = stack.pop()
    if visit[node]: continue
    else: visit[node] = True
    print(node, end=" ")

    for adj_node in sorted(graph[node], reverse=True):
        if not visit[adj_node]:
            stack.append(adj_node)

print()

queue = collections.deque()
visit = [False for i in range(N + 1)]

queue.append(V)
while queue:
    node = queue.popleft()
    if visit[node]: continue
    else: visit[node] = True
    print(node, end=" ")

    for adj_node in sorted(graph[node], reverse=False):
        if not visit[adj_node]:
            queue.append(adj_node)


