import sys
def input(): return sys.stdin.readline().rstrip()


N, B = list(map(int, input().split()))
matrix = []
dp = dict()

for _ in range(N):
	matrix.append(list(map(int, input().split())))


def mult(mat1, mat2):
	n = len(mat1)
	ret = [[0] * n for _ in range(n)]

	for r in range(n):
		for c in range(n):
			row_line = mat1[r]
			col_line = [mat2[i][c] for i in range(n)]
			ret[r][c] = sum([row_line[i] * col_line[i] for i in range(n)]) % 1000

	return ret

def power(mat, n):
	if n in dp: return dp[n]

	if n == 1:
		ret = [[e % 1000 for e in line] for line in mat]
	elif n % 2 == 0:
		ret = mult(power(mat, n // 2), power(mat, n // 2))
	else:
		ret = mult(power(mat, n // 2), power(mat, n // 2 + 1))

	dp[n] = ret
	return dp[n]


for line in power(matrix, B):
	print(*line, sep=" ")
