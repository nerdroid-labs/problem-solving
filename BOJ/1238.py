import collections
import heapq
import sys
def input(): return sys.stdin.readline().rstrip()


N, M, X = list(map(int, input().split()))
graph = collections.defaultdict(list)
dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
	s, t, w = list(map(int, input().split()))
	graph[s].append((t, w))

for S in range(1, N + 1):
	dist[S][S] = 0

	heap = []
	heapq.heappush(heap, (0, S))

	while heap:
		w, node = heapq.heappop(heap)

		for adj, adj_w in graph[node]:
			if dist[S][adj] > w + adj_w:
				dist[S][adj] = w + adj_w
				heapq.heappush(heap, (dist[S][adj], adj))

answer = -1
for n in range(1, N + 1):
	answer = max(answer, dist[n][X] + dist[X][n])

print(answer)
