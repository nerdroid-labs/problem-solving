import sys
import itertools


def input():
	return sys.stdin.readline().rstrip()


def get_dist(x, y):
	return abs(x[0] - y[0]) + abs(x[1] - y[1])


N, M = list(map(int, input().split()))
home = []
chicken = []

for r in range(N):
	line = list(map(int, input().split()))

	for c in range(N):
		if line[c] == 1:
			home.append((r, c))
		elif line[c] == 2:
			chicken.append((r, c))

answer = sys.maxsize
for chick in itertools.combinations(chicken, M):
	dist = [sys.maxsize] * len(home)

	for i in range(len(home)):
		for chic in chick:
			dist[i] = min(dist[i], get_dist(home[i], chic))

	answer = min(answer, sum(dist))

print(answer)
