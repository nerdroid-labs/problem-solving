import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
in_degree = [0 for _ in range(N + 1)]
out_degree = [[] for _ in range(N + 1)]

for _ in range(M):
	s, t = list(map(int, input().split()))

	in_degree[t] += 1
	out_degree[s].append(t)

queue = collections.deque()
visit = [False] * (N + 1)
answer = []

for i in range(1, N + 1):
	if not in_degree[i]:
		queue.append(i)
		visit[i] = True

while queue:
	node = queue.popleft()
	answer.append(node)

	for out in out_degree[node]:
		in_degree[out] -= 1

	for i in range(1, N + 1):
		if not visit[i] and not in_degree[i]:
			visit[i] = True
			queue.append(i)

print(*answer, sep=" ")
