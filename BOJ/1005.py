import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


def remove_all_in_degree(x):
	global in_edges, build_time, dp

	if dp[x] is not None:
		return dp[x]

	require = 0
	for edge in in_edges[x]:
		require = max(remove_all_in_degree(edge), require)

	dp[x] = build_time[x] + require
	return build_time[x] + require


T = int(input())
for _ in range(T):
	N, K = list(map(int, input().split()))
	build_time = [-1] + list(map(int, input().split()))
	in_edges = collections.defaultdict(list)
	dp = [None] * (N + 1)

	for _ in range(K):
		X, Y = list(map(int, input().split()))
		in_edges[Y].append(X)

	W = int(input())
	answer = remove_all_in_degree(W)
	print(answer)
