import sys
sys.setrecursionlimit(10 ** 5)


def input():
	return sys.stdin.readline().rstrip()


def dfs(r, c, visit, height):
	global N, m

	for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		nr, nc = dr + r, dc + c

		if 0 <= nr < N and 0 <= nc < N and m[nr][nc] > height and not visit[nr][nc]:
			visit[nr][nc] = True
			dfs(nr, nc, visit, height)


N = int(input())
m = []

max_height = -1
answer = -1
for _ in range(N):
	m.append(list(map(int, input().split())))
	max_height = max(max_height, max(m[-1]))

for height in range(max_height + 1):
	visit = [[False] * N for _ in range(N)]
	ctr = 0

	for r in range(N):
		for c in range(N):
			if m[r][c] > height and not visit[r][c]:
				ctr += 1
				visit[r][c] = True
				dfs(r, c, visit, height)

	answer = max(answer, ctr)

print(answer)
