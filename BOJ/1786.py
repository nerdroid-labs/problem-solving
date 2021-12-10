import sys
def input(): return sys.stdin.readline().rstrip()


T = input()
P = input()

table = [0] * len(P)
p_idx = 0

for t_idx in range(1, len(P)):
	while p_idx > 0 and P[p_idx] != P[t_idx]:
		p_idx = table[p_idx - 1]

	if P[p_idx] == P[t_idx]:
		p_idx += 1
		table[t_idx] = p_idx


answer = []
p_idx = 0
for t_idx in range(len(T)):
	while p_idx > 0 and T[t_idx] != P[p_idx]:
		p_idx = table[p_idx - 1]

	if P[p_idx] == T[t_idx]:
		if p_idx == len(P) - 1:
			p_idx = table[p_idx]
			answer.append(t_idx - (len(P) - 1) + 1)
		else:
			p_idx += 1

print(len(answer))
print(*answer, sep="\n")
