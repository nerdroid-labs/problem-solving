import sys


def input():
	return sys.stdin.readline().rstrip()


N, M, R = list(map(int, input().split()))
items = list(map(int, input().split()))
items = [-1] + items
dists = [[sys.maxsize] * (N + 1) for _ in range(N + 1)]

for _ in range(R):
	s, t, w = list(map(int, input().split()))
	dists[s][t] = min(dists[s][t], w)
	dists[t][s] = min(dists[t][s], w)

for i in range(1, N + 1):
	dists[i][i] = 0

for i in range(1, N + 1):
	for j in range(1, N + 1):
		for t in range(1, N + 1):
			dists[j][t] = min(dists[j][t], dists[j][i] + dists[i][t])

answer = -1
for dist in dists:
	sub_answer = 0
	for i in range(1, N + 1):
		if dist[i] <= M:
			sub_answer += items[i]

	answer = max(sub_answer, answer)

print(answer)
