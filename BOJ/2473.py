import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = (sys.maxsize, sys.maxsize, sys.maxsize)

for s in range(N - 2):
	l = s + 1
	r = N - 1

	while l < r:
		if abs(sum(answer)) > abs(nums[s] + nums[l] + nums[r]):
			answer = (nums[s], nums[l], nums[r])

		if nums[s] + nums[l] + nums[r] > 0:
			r -= 1

		else:
			l += 1

print(*answer, sep=" ")
