import math
import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
target = [c for c in input().split()]
circle = [c for c in input().split()] * 2
circle.pop()

table = [0] * len(target)
p_idx = 0

for t_idx in range(1, len(target)):
	while p_idx > 0 and target[p_idx] != target[t_idx]:
		p_idx = table[p_idx - 1]

	if target[p_idx] == target[t_idx]:
		p_idx += 1
		table[t_idx] = p_idx

p_idx = 0
ctr = 0
for t_idx in range(len(circle)):
	while p_idx > 0 and circle[p_idx] != circle[t_idx]:
		p_idx = table[p_idx - 1]

	if circle[p_idx] == circle[t_idx]:
		if p_idx == len(target) - 1:
			ctr += 1
			p_idx = table[p_idx]
		else:
			p_idx += 1

gcd = math.gcd(N, ctr)
print(f"{ctr // gcd}/{N // gcd}")
