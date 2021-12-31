import collections
import itertools
import sys


def input():
	return sys.stdin.readline().rstrip()


def bfs(r, c, visit):
	global N, M, matrix

	area = 0
	virus = False
	queue = collections.deque()
	queue.append((r, c))
	visit[r][c] = True

	while queue:
		r, c = queue.popleft()
		area += 1

		for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
			nr, nc = dr + r, dc + c

			if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc]:
				if matrix[nr][nc] == 0:
					visit[nr][nc] = True
					queue.append((nr, nc))

				elif matrix[nr][nc] == 2:
					visit[nr][nc] = True
					queue.append((nr, nc))
					virus = True

	return 0 if virus else area


N, M = list(map(int, input().split()))
matrix = []
possibles = []

for r in range(N):
	matrix.append(list(map(int, input().split())))
	for c in range(M):
		if matrix[r][c] == 0:
			possibles.append((r, c))

answer = -1
for comb in itertools.combinations(possibles, 3):
	for r, c in comb:
		matrix[r][c] = 1

	sub_answer = 0
	visit = [[False] * M for _ in range(N)]

	for r in range(N):
		for c in range(M):
			if matrix[r][c] == 0 and not visit[r][c]:
				sub_answer += bfs(r, c, visit)

	answer = max(answer, sub_answer)

	for r, c in comb:
		matrix[r][c] = 0

print(answer)
