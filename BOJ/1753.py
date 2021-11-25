import heapq
import sys
import collections
def input(): return sys.stdin.readline().rstrip()


V, E = list(map(int, input().split()))
S = int(input())

graph = collections.defaultdict(list)
for _ in range(E):
    s, t, w = list(map(int, input().split()))
    graph[s].append((w, t))

dist = [float('inf')] * (V + 1)
dist[S] = 0
heap = []
heapq.heappush(heap, (dist[S], S))

while heap:
    w, node = heapq.heappop(heap)

    for adj_w, adj in graph[node]:
        if dist[adj] > w + adj_w:
            dist[adj] = w + adj_w
            heapq.heappush(heap, (dist[adj], adj))

for d in dist[1:]:
    if d == float('inf'): print("INF")
    else: print(d)
