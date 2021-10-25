import bisect
import sys
input = sys.stdin.readline

input()
coords = list(map(int, input().split()))
coords_ordered = sorted(set(coords))

for coord in coords:
    print(bisect.bisect_left(coords_ordered, coord), end=" ")
