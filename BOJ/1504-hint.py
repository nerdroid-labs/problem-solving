import collections
import heapq
import sys
def input(): return sys.stdin.readline().rstrip()


N, E = list(map(int, input().split()))
graph = collections.defaultdict(dict)

for _ in range(E):
	a, b, c = list(map(int, input().split()))
	graph[a][b] = graph[b][a] = min(graph[b].get(a, float('inf')), c)

v1, v2 = list(map(int, input().split()))


def dijkstra(node):
	dist = [float('inf')] * (N + 1)
	dist[node] = 0

	pq = []
	heapq.heappush(pq, (dist[node], node))

	while pq:
		w, node = heapq.heappop(pq)

		for next_node, next_w in graph[node].items():
			if dist[next_node] > next_w + w:
				dist[next_node] = next_w + w
				heapq.heappush(pq, (dist[next_node], next_node))

	return dist


dist = collections.defaultdict(list)
dist[1] = dijkstra(1)
dist[v1] = dijkstra(v1)
dist[v2] = dijkstra(v2)

case_v1_v2 = dist[1][v1] + dist[v1][v2] + dist[v2][N]
case_v2_v1 = dist[1][v2] + dist[v2][v1] + dist[v1][N]
answer = min(case_v1_v2, case_v2_v1)

if answer == float('inf'): print(-1)
else: print(answer)
