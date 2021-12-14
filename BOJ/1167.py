import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


def bfs(node, visit, total_weight):
	global answer, farthest, graph

	if answer < total_weight:
		answer = total_weight
		farthest = node

	for neighbor, weight in graph[node]:
		if not visit[neighbor]:
			visit[neighbor] = True
			bfs(neighbor, visit, total_weight + weight)
			visit[neighbor] = False


N = int(input())
answer = float('-inf')
farthest = None
graph = collections.defaultdict(list)
for _ in range(N):
	line = list(map(int, input().split()))
	node = line[0]

	for i in range(1, len(line) - 1, 2):
		neighbor, weight = line[i], line[i + 1]
		graph[node].append((neighbor, weight))

visit = [False] * (N + 1)
visit[1] = True
bfs(1, visit, 0)

visit = [False] * (N + 1)
visit[farthest] = True
bfs(farthest, visit, 0)

print(answer)
