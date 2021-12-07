import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
matrix = []
parents = {0: (0, 1), 1: (0, 1, 2), 2: (1, 2)}

dp_min = None
dp_max = None
for row in range(N):
	line = list(map(int, input().split()))
	if row == 0:
		dp_min = line[:]
		dp_max = line[:]
	else:
		dp_min_next = dp_min[:]
		dp_max_next = dp_max[:]
		for col in range(3):
			dp_max_next[col] = line[col] + max([dp_max[parent] for parent in parents[col]])
			dp_min_next[col] = line[col] + min([dp_min[parent] for parent in parents[col]])

		dp_min = dp_min_next[:]
		dp_max = dp_max_next[:]

print(max(dp_max), min(dp_min))
