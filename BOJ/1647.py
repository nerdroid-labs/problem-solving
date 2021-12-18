import sys


def input():
	return sys.stdin.readline().rstrip()


def find(parents, x):
	if parents[x] == x:
		return x
	else:
		return find(parents, parents[x])


def union(parents, x, y):
	x = find(parents, x)
	y = find(parents, y)

	if x < y:
		parents[y] = x
	else:
		parents[x] = y


N, M = list(map(int, input().split()))
edges = []

for _ in range(M):
	edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[-1])
parents = [i for i in range(N + 1)]
answer = []

for s, t, w in edges:
	if find(parents, s) != find(parents, t):
		answer.append(w)
		union(parents, s, t)

print(sum(answer) - max(answer))
