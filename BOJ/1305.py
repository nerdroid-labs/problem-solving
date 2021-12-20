import sys


def input():
	return sys.stdin.readline().rstrip()


L = int(input())
pattern = input()

table = [0] * len(pattern)
p_idx = 0

for t_idx in range(1, len(pattern)):
	while p_idx > 0 and pattern[p_idx] != pattern[t_idx]:
		p_idx = table[p_idx - 1]

	if pattern[p_idx] == pattern[t_idx]:
		p_idx += 1
		table[t_idx] = p_idx

print(L - table[-1])
