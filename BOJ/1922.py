import sys


def input():
	return sys.stdin.readline().rstrip()


def find(x):
	if x == parents[x]:
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


N = int(input())
M = int(input())
edges = []
parents = [i for i in range(N + 1)]

for _ in range(M):
	edges.append(list(map(int, input().split())))

edges.sort(key=lambda x: x[-1])

answer = 0
for s, t, w in edges:
	if find(s) != find(t):
		answer += w
		union(s, t)

print(answer)
