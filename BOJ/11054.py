import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
A = list(map(int, input().split()))

dp_up = [0] * N
dp_down = [0] * N
for k in range(N):
	a_k = A[k]

	best = -1
	for i in range(k - 1, -1, -1):
		a_i = A[i]
		if a_i < a_k and best < dp_up[i]:
			best = dp_up[i]

	dp_up[k] = best + 1

for k in range(N - 1, -1, -1):
	a_k = A[k]

	best = -1
	for i in range(k, N):
		a_i = A[i]
		if a_k > a_i and best < dp_down[i]:
			best = dp_down[i]

	dp_down[k] = best + 1

results = [dp_up[i] + dp_down[i] + 1 for i in range(N)]
print(max(results))
