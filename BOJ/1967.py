import sys
import collections
def input(): return sys.stdin.readline().rstrip()


N = int(input())
graph = collections.defaultdict(list)

for _ in range(N - 1):
    s, t, w = list(map(int, input().split()))
    graph[s].append((t, w))
    graph[t].append((s, w))

answer = 0
for n in range(1, N):
    visit = [False] * (N + 1)
    queue = collections.deque()

    queue.append((n, 0))
    while queue:
        node, dist = queue.popleft()
        visit[node] = True
        answer = max(answer, dist)

        for adj, weight in graph[node]:
            if not visit[adj]:
                queue.append((adj, dist + weight))

print(answer)
