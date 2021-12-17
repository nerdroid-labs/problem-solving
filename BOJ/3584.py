import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


def get_ancestors(parents, n):
	ancestors = [n]

	while n != parents[n]:
		ancestors.append(parents[n])
		n = parents[n]

	return ancestors


T = int(input())
for _ in range(T):
	N = int(input())
	graph = collections.defaultdict(list)

	parents = [i for i in range(N + 1)]
	for _ in range(N - 1):
		s, t = list(map(int, input().split()))
		parents[t] = s

	n1, n2 = list(map(int, input().split()))
	n1_ancestors = get_ancestors(parents, n1)
	n2_ancestors = get_ancestors(parents, n2)

	for ancestor in n1_ancestors:
		if ancestor in n2_ancestors:
			print(ancestor)
			break
