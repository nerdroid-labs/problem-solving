import sys
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
dist = [float('inf')] * (N + 1)
dist[1] = 0
edges = []

for _ in range(M):
	edges.append(list(map(int, input().split())))


for _ in range(N - 1):
	for s, t, w in edges:
		dist[t] = min(dist[t], dist[s] + w)

for s, t, w in edges:
	if dist[t] > dist[s] + w:
		print(-1)
		exit(0)

for t in range(2, N + 1):
	if dist[t] == float('inf'):
		print(-1)
	else:
		print(dist[t])
