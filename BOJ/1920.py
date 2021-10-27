import bisect
import sys

input = sys.stdin.readline

input()
A = list(map(int, input().split()))
A.sort()

input()
B = list(map(int, input().split()))

for b in B:
    left = bisect.bisect_left(A, b)
    right = bisect.bisect_right(A, b)
    print(int(right - left > 0))
