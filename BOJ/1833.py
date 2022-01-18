import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
cost = 0
road = []
parents = [i for i in range(N)]


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


weights = []
for s in range(N):
	for t, w in enumerate(list(map(int, input().split()))):
		if t <= s:
			continue

		elif w > 0:
			weights.append((s, t, w))
		else:
			union(s, t)
			cost += abs(w)

weights.sort(key=lambda x: x[-1])

for s, t, w in weights:
	if find(s) != find(t):
		road.append((s + 1, t + 1))
		cost += w
		union(s, t)

print(cost, len(road))
for r in road:
	print(*r, sep=" ")
