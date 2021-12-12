import sys
def input(): return sys.stdin.readline().rstrip()


N, K = list(map(int, input().split()))
codes = []

for _ in range(N):
	input()
	codes.append(list(input().split()))

sets = []
for i in range(N):
	st = set()
	l = len(codes[i])

	for s in range(l):
		if s + K > l: break
		sliced = codes[i][s:s+K]
		st.add(" ".join(sliced))
		st.add(" ".join(sliced[::-1]))

	sets.append(st)

intersect = sets[0]
for s in sets[1:]:
	intersect &= s

if intersect:
	print("YES")
else:
	print("NO")
