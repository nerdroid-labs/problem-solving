import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


R, C, T = list(map(int, input().split()))
matrix = []
air_purifier = []

for r in range(R):
	matrix.append(list(matrix(int, input().split())))
	for c in range(C):
		if matrix[r][c] == -1:
			air_purifier.append((r, c))

up, down = air_purifier
for _ in range(T):
	# diffuse
	change = collections.defaultdict(int)
	for r in range(R):
		for c in range(C):
			if matrix[r][c] > 0:
				ctr = 0
				for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
					nr, nc = dr + r, dc + c

					if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] >= 0:
						change[(nr, nc)] += matrix[r][c] // 5
						ctr += 1

				change[(r, c)] -= ctr * (matrix[r][c] // 5)

	for r, c in change.keys():
		matrix[r][c] += change[(r, c)]

	r, c = up
	r -= 1
	direction = 0
	while True:
		if direction == 0:
			if r - 1 < 0:
				direction += 1
				continue
			else:
				matrix[r][c] = matrix[r - 1][c]
				r -= 1

		if direction == 1:
			if c + 1 > C - 1:
				direction += 1
				continue
			else:
				matrix[r][c] = matrix[r][c + 1]
				c += 1

		if direction == 2:
			if r + 1 > up[0]:
				direction += 1
				continue
			else:
				matrix[r][c] = matrix[r + 1][c]
				r += 1

		if direction == 3:
			if c == 1:
				matrix[r][c] = 0
				break
			else:
				matrix[r][c] = matrix[r][c - 1]
				c -= 1

	r, c = down
	r += 1
	direction = 0
	while True:
		if direction == 0:
			if r + 1 == R:
				direction += 1
				continue
			else:
				matrix[r][c] = matrix[r + 1][c]
				r += 1

		if direction == 1:
			if c + 1 == C:
				direction += 1
				continue
			else:
				matrix[r][c] = matrix[r][c + 1]
				c += 1

		if direction == 2:
			if r - 1 == down[0] - 1:
				direction += 1
				continue
			else:
				matrix[r][c] = matrix[r - 1][c]
				r -= 1

		if direction == 3:
			if c == 1:
				matrix[r][c] = 0
				break
			else:
				matrix[r][c] = matrix[r][c - 1]
				c -= 1

print(sum([sum(line) for line in matrix]) + 2)
