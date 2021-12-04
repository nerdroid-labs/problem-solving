import sys
import heapq
import collections
def input(): return sys.stdin.readline().rstrip()


N = int(input())
M = int(input())

dist = [float('inf')] * (N + 1)
graph = [[float('inf')] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
	s, t, w = list(map(int, input().split()))
	graph[s][t] = min(w, graph[s][t])

A, B = list(map(int, input().split()))
pq = []
heapq.heappush(pq, (0, A))
dist[A] = 0

while pq:
	w, node = heapq.heappop(pq)

	for i in range(1, N + 1):
		if graph[node][i] != float('inf') and w + graph[node][i] < dist[i]:
			dist[i] = w + graph[node][i]
			heapq.heappush(pq, (dist[i], i))

print(dist[B])
