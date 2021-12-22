import sys


def input():
	return sys.stdin.readline().rstrip()


text = input()
answer = 0

for i in range(len(text)):
	pattern = text[i:]
	p_idx = 0
	table = [0] * len(pattern)

	for t_idx in range(1, len(pattern)):
		while p_idx > 0 and pattern[p_idx] != pattern[t_idx]:
			p_idx = table[p_idx - 1]

		if pattern[p_idx] == pattern[t_idx]:
			p_idx += 1
			table[t_idx] = p_idx

	answer = max(answer, max(table))

print(answer)
