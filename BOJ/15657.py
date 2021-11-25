import sys
import itertools
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

for comb in itertools.combinations_with_replacement(nums, M):
    print(*comb, sep=" ")
