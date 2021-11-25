import sys
import itertools
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

for perm in itertools.permutations(nums, M):
    print(*perm, sep=" ")
