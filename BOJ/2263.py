import sys
sys.setrecursionlimit(10 ** 5)

def input():
	return sys.stdin.readline().rstrip()

N = int(input())
in_orders = list(map(int, input().split()))
post_orders = list(map(int, input().split()))


def print_root(in_start, in_end, post_start, post_end):
	root = post_orders[post_end]
	root_idx = in_orders.index(root)

	print(root, end=" ")

	left_diff = root_idx - in_start
	right_diff = in_end - root_idx

	if left_diff > 0:
		print_root(in_start, root_idx - 1, post_start, post_start + left_diff - 1)

	if right_diff > 0:
		print_root(root_idx + 1, in_end, post_end - right_diff, post_end - 1)


print_root(0, N - 1, 0, N - 1)
print()
