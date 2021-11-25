import sys
import itertools
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

combinations = list(set(itertools.combinations_with_replacement(nums, M)))
combinations.sort()

for comb in combinations:
    print(*comb, sep=" ")
