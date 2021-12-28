# https://hbj0209.tistory.com/143
import sys


def input():
	return sys.stdin.readline().rstrip()


N, S = list(map(int, input().split()))
nums = list(map(int, input().split()))

answer = sys.maxsize
s, e = 0, 0
total = nums[0]

while True:
	if total >= S:
		answer = min(answer, e - s + 1)
		total -= nums[s]
		s += 1
	else:
		e += 1
		if e == N:
			break
		else:
			total += nums[e]

print(answer if answer != sys.maxsize else 0)
