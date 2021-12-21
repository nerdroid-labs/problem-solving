import sys


def input():
	return sys.stdin.readline().rstrip()


pattern, N = input().split()
N = int(N)

table = [0] * len(pattern)
p_idx = 0

for t_idx in range(1, len(pattern)):
	while p_idx > 0 and pattern[p_idx] != pattern[t_idx]:
		p_idx = table[p_idx - 1]

	if pattern[p_idx] == pattern[t_idx]:
		p_idx += 1
		table[t_idx] = p_idx

print(len(pattern) + (len(pattern) - table[-1]) * (N - 1))
