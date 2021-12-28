import sys


def input():
	return sys.stdin.readline().rstrip()


def find(x):
	global parents

	if parents[x] == x:
		return x
	else:
		return find(parents[x])


def union(x, y):
	global parents

	x = find(x)
	y = find(y)

	if x < y:
		parents[y] = x
	else:
		parents[x] = y


N = int(input())
nodes = []
edges = []
parents = [i for i in range(N)]

for _ in range(N):
	nodes.append(tuple(map(float, input().split())))

for i in range(N - 1):
	for j in range(i + 1, N):
		node_1 = nodes[i]
		node_2 = nodes[j]
		w = ((node_1[0] - node_2[0]) ** 2 + (node_1[1] - node_2[1]) ** 2) ** 0.5
		edges.append((i, j, w))

answer = 0
edges.sort(key=lambda x: x[-1])
for s, t, w in edges:
	if find(s) != find(t):
		answer += w
		union(s, t)

print(f"{answer:.2f}")
