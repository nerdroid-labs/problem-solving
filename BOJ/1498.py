import sys


def input():
	return sys.stdin.readline().rstrip()


pattern = input()
table = [0] * len(pattern)

p_idx = 0
for t_idx in range(1, len(pattern)):
	while p_idx > 0 and pattern[p_idx] != pattern[t_idx]:
		p_idx = table[p_idx - 1]

	if pattern[p_idx] == pattern[t_idx]:
		p_idx += 1
		table[t_idx] = p_idx


for i, e in enumerate(table, start=1):
	x_len = i - e
	if i % x_len == 0 and i // x_len > 1:
		print(i, i // x_len)
