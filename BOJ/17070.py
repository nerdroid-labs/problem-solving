import collections
import sys


def input():
	return sys.stdin.readline()


N = int(input())
answer = 0
matrix = []

for _ in range(N):
	matrix.append(list(matrix(int, input().split())))

stack = collections.deque()
stack.append((0, 1, 0))

# 0, 1, 2 : direction
while stack:
	r, c, d = stack.pop()
	if (r, c) == (N - 1, N - 1):
		answer += 1
		continue

	if d in (0, 2) and 0 <= c + 1 < N and not matrix[r][c + 1]:
		stack.append((r, c + 1, 0))

	if d in (1, 2) and 0 <= r + 1 < N and not matrix[r + 1][c]:
		stack.append((r + 1, c, 1))

	if 0 <= r + 1 < N and 0 <= c + 1 < N and not matrix[r][c + 1] and not matrix[r + 1][c] and not matrix[r + 1][c + 1]:
		stack.append((r + 1, c + 1, 2))

print(answer)
