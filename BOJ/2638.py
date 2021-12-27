import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


def bfs(start_r, start_c):
	global matrix, air_group
	queue = collections.deque()
	queue.append((start_r, start_c))

	while queue:
		r, c = queue.popleft()

		for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nr, nc = r + dr, c + dc

			if 0 <= nr < N and 0 <= nc < M and not matrix[nr][nc] and not air_group[nr][nc]:
				air_group[nr][nc] = True
				queue.append((nr, nc))


h = 0
N, M = list(map(int, input().split()))
air_group = [[False] * M for _ in range(N)]
matrix = []

for _ in range(N):
	matrix.append(list(map(int, input().split())))

bfs(0, 0)

while True:
	melts = []
	cheese = False
	for r in range(N):
		for c in range(M):
			if matrix[r][c] == 1:
				cheese = True
				ctr = 0

				for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
					nr, nc = r + dr, c + dc
					if 0 <= nr < N and 0 <= nc < M and air_group[nr][nc]:
						ctr += 1

				if ctr >= 2:
					melts.append((r, c))

	if not cheese:
		break
	else:
		for r, c in melts:
			air_group[r][c] = True
			matrix[r][c] = 0
			bfs(r, c)

		h += 1

print(h)
