import sys
def input(): return sys.stdin.readline().rstrip()


def failure(pattern):
	table = [0] * len(pattern)

	p_idx = 0
	for t_idx in range(1, len(pattern)):
		while p_idx > 0 and pattern[t_idx] != pattern[p_idx]:
			p_idx = table[p_idx - 1]

		if pattern[p_idx] == pattern[t_idx]:
			p_idx += 1
			table[t_idx] = p_idx

	return table


text = input()
pattern = input()

table = failure(pattern)
answer = 0
p_idx = 0

for t_idx in range(len(text)):
	while p_idx > 0 and text[t_idx] != pattern[p_idx]:
		p_idx = table[p_idx - 1]

	if text[t_idx] == pattern[p_idx]:
		if p_idx == len(pattern) - 1:
			answer = 1
			break
		else:
			p_idx += 1

print(answer)
