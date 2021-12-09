import sys
def input(): return sys.stdin.readline().rstrip()


V, E = list(map(int, input().split()))
edges = []

for _ in range(E):
	edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[-1])
parents = [i for i in range(V + 1)]


def find(x):
	if parents[x] == x:
		return x
	else:
		return find(parents[x])


def union(x, y):
	x = find(x)
	y = find(y)

	if x < y:
		parents[y] = x
	else:
		parents[x] = y


weights = 0
for s, t, e in edges:
	if find(s) != find(t):
		weights += e
		union(s, t)

print(weights)
