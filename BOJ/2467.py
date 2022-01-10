import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
nums = list(map(int, input().split()))
answer = (sys.maxsize, sys.maxsize)

e = N - 1
for s in range(N - 1):
	if s == e:
		break

	while abs(nums[s] + nums[e]) > abs(nums[s] + nums[e - 1]) and e - 1 != s:
		e -= 1

	if abs(sum(answer)) > abs(nums[s] + nums[e]):
		answer = (nums[s], nums[e])

print(*answer, sep=" ")
