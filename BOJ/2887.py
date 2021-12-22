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


N = int(input())
planets = [[], [], []]
edges = []
parents = [i for i in range(N)]

for i in range(N):
	for p, e in enumerate(list(map(int, input().split()))):
		planets[p].append((i, e))

for p in planets:
	p.sort(key=lambda x: x[-1])

	for i in range(N - 1):
		v1, w1 = p[i]
		v2, w2 = p[i + 1]
		edges.append((v1, v2, abs(w1 - w2)))
		edges.append((v2, v1, abs(w1 - w2)))

edges.sort(key=lambda x:x[-1])

answer = 0
for s, t, w in edges:
	if find(parents, s) != find(parents, t):
		answer += w
		union(parents, s, t)

print(answer)
