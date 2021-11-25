import sys
import itertools
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums.sort()

permutations = list(set(itertools.permutations(nums, M)))
permutations.sort()

for perm in permutations:
    print(*perm, sep=" ")
