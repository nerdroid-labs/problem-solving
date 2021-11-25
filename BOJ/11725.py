import sys
import collections
def input(): return sys.stdin.readline().rstrip()


graph = collections.defaultdict(list)
N = int(input())
for _ in range(N - 1):
    s, t = list(map(int, input().split()))
    graph[s].append(t)
    graph[t].append(s)

parent = [-1] * (N + 1)
visit = [False] * (N + 1)
queue = collections.deque()
queue.append(1)

while queue:
    node = queue.popleft()
    if visit[node]: continue
    else: visit[node] = True

    for child in graph[node]:
        if not visit[child]:
            queue.append(child)
            parent[child] = node

print(*parent[2:], sep="\n")
