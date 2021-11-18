import collections

N, M = list(map(int, input().rstrip().split()))
graph = dict()

for _ in range(N + M):
    s, t = tuple(map(int, input().rstrip().split()))
    graph[s] = t

visited = [False] * (100 + 1)
queue = collections.deque()
queue.append((1, 0))

while queue:
    node, dist = queue.popleft()
    if node == 100:
        print(dist)
        break

    elif visited[node]: continue
    else:
        visited[node] = True

        for m in range(1, 6 + 1):
            if 1 <= node + m <= 100 and not visited[node + m]:
                if (node + m) in graph: queue.append((graph[node + m], dist + 1))
                else: queue.append((node + m, dist + 1))
