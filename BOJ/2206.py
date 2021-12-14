import collections
import sys
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
matrix = []
answer = float('inf')

for _ in range(N):
	matrix.append(list(map(int, input())))


def bfs():
	global answer, matrix

	visit = [[[False, False] for __ in range(M)] for _ in range(N)]
	queue = collections.deque()
	NOT_CRASHED, CRASHED = 0, 1

	queue.append((0, 0, 1, NOT_CRASHED))
	visit[0][0][0] = True

	while queue:
		r, c, w, crash = queue.popleft()
		if r == N - 1 and c == M - 1:
			answer = min(answer, w)

		for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nr, nc = dr + r, dc + c
			if 0 <= nr < N and 0 <= nc < M:
				if not matrix[nr][nc] and not visit[nr][nc][crash]:
					visit[nr][nc][crash] = True
					queue.append((nr, nc, w + 1, crash))

				if matrix[nr][nc] and crash == NOT_CRASHED and not visit[nr][nc][CRASHED]:
					visit[nr][nc][CRASHED] = True
					queue.append((nr, nc, w + 1, CRASHED))

bfs()

if answer == float('inf'):
	print(-1)
else:
	print(answer)
