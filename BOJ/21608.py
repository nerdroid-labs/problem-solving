import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
seats = [[None] * N for _ in range(N)]
wanna = dict()

for _ in range(N ** 2):
	line = list(map(int, input().split()))
	n, likes = line[0], line[1:]
	wanna[n] = likes

	like_num = float('-inf')
	blank_num = float('-inf')
	next_r, next_c = None, None
	for r in range(N):
		for c in range(N):
			if seats[r][c]: continue

			like = 0
			blank = 0
			for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
				nr, nc = r + dr, c + dc
				if 0 <= nr < N and 0 <= nc < N:
					if not seats[nr][nc]: blank += 1
					elif seats[nr][nc] in likes: like += 1

			if like_num < like:
				like_num = like
				blank_num = blank
				next_r, next_c = r, c

			elif like_num == like and blank_num < blank:
				blank_num = blank
				next_r, next_c = r, c

	seats[next_r][next_c] = n

answer = 0
feedback = [0, 1, 10, 100, 1000]
for r in range(N):
	for c in range(N):
		n = seats[r][c]
		match = 0
		for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
			nr, nc = r + dr, c + dc
			if 0 <= nr < N and 0 <= nc < N and seats[nr][nc] in wanna[n]:
				match += 1

		answer += feedback[match]

print(answer)
