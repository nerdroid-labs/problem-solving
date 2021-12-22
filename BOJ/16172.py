import sys


def input():
	return sys.stdin.readline().rstrip()


text = "".join([c for c in input() if c.isalpha()])
pattern = input()

table = [0] * len(pattern)
p_idx = 0

for t_idx in range(1, len(pattern)):
	while p_idx > 0 and pattern[p_idx] != pattern[t_idx]:
		p_idx = table[p_idx - 1]

	if pattern[p_idx] == pattern[t_idx]:
		p_idx += 1
		table[t_idx] = p_idx


found = False
p_idx = 0
for t_idx in range(len(text)):
	while p_idx > 0 and pattern[p_idx] != text[t_idx]:
		p_idx = table[p_idx - 1]

	if pattern[p_idx] == text[t_idx]:
		if p_idx == len(pattern) - 1:
			p_idx = table[p_idx]
			found = True
		else:
			p_idx += 1

if found:
	print(1)
else:
	print(0)
