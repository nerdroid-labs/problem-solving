import sys


def input():
	return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
parent = [i for i in range(N)]


def find(x):
	if parent[x] != x:
		return find(parent[x])
	else:
		return x


def union(x, y):
	x = find(x)
	y = find(y)

	if x < y:
		parent[y] = x
	else:
		parent[x] = y


ctr = 0
is_cycle = False
for _ in range(M):
	x, y = list(map(int, input().split()))
	ctr += 1

	if find(x) != find(y):
		union(x, y)
	else:
		is_cycle = True
		break

print(ctr if is_cycle else 0)
