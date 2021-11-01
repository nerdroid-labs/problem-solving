import sys
import itertools

input = sys.stdin.readline
N, K = list(map(int, input().split()))

print(len(list(itertools.combinations(range(N), K))))
