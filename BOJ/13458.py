import math
import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
nums = list(map(int, input().split()))
B, C = list(map(int, input().split()))

ctrs = [1] * N
nums = [max(0, n - B) for n in nums]

for i in range(N):
	ctrs[i] += int(math.ceil(nums[i] / C))

print(sum(ctrs))
