import sys
def input():return sys.stdin.readline().rstrip()


TC = int(input())

inf = 10 ** 9
for _ in range(TC):
	N, M, W = list(map(int, input().split()))
	parents = [i for i in range(N + 1)]
	edges = []

	for _ in range(M):
		s, e, t = list(map(int, input().split()))
		edges.append((s, e, t))
		edges.append((e, s, t))

	for _ in range(W):
		s, e, t = list(map(int, input().split()))
		edges.append((s, e, -t))

	dists = [inf] * (N + 1)
	dists[1] = 0

	possible = False
	for i in range(N):
		for s, e, t in edges:
			if dists[e] > dists[s] + t:
				dists[e] = dists[s] + t
				if i == N - 1:
					possible = True

	if possible:
		print("YES")
	else:
		print("NO")
