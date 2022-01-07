import sys


def input():
	return sys.stdin.readline().rstrip()


R, C = list(map(int, input().split()))
answer = 0
diff = ((1, 0), (-1, 0), (0, 1), (0, -1))
alpha = [False] * 26
matrix = [[ord(c) - ord('A') for c in input()] for _ in range(R)]


def dfs(r, c, times):
	global answer
	answer = max(answer, times)

	for dr, dc in diff:
		nr, nc = r + dr, c + dc

		if 0 <= nr < R and 0 <= nc < C and not alpha[matrix[nr][nc]]:
			alpha[matrix[nr][nc]] = True
			dfs(nr, nc, times + 1)
			alpha[matrix[nr][nc]] = False


alpha[matrix[0][0]] = True
dfs(0, 0, 1)
print(answer)
