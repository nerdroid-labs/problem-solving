import collections
import heapq
import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
M = int(input())
dist = [float('inf')] * (N + 1)
graph = collections.defaultdict(dict)

for _ in range(M):
	s, t, w = list(map(int, input().split()))
	graph[s].setdefault(t, float('inf'))
	graph[s][t] = min(graph[s][t], w)

A, B = list(map(int, input().split()))
dist[A] = 0

pq = []
parent = [i for i in range(N + 1)]
heapq.heappush(pq, (0, A))

while pq:
	w, node = heapq.heappop(pq)

	# if w > dist[node]:
	# 	continue

	for adj, adj_w in graph[node].items():
		if adj_w + w < dist[adj]:
			dist[adj] = adj_w + w
			parent[adj] = node
			heapq.heappush(pq, (dist[adj], adj))

path = collections.deque([B])
while path[0] != A:
	path.appendleft(parent[path[0]])

print(dist[B])
print(len(path))
print(*path, sep=" ")
