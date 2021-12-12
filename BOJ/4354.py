import sys
def input(): return sys.stdin.readline().rstrip()

while True:
	s = input()
	if s == ".":
		break

	table = [0] * len(s)
	p_idx = 0
	for t_idx in range(1, len(s)):
		while p_idx > 0 and s[t_idx] != s[p_idx]:
			p_idx = table[p_idx - 1]

		if s[t_idx] == s[p_idx]:
			p_idx += 1
			table[t_idx] = p_idx

	last = table[-1]
	repeat_len = len(s) - last

	if last % repeat_len == 0:
		print(len(s) // repeat_len)
	else:
		print(1)
