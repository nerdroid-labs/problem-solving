import sys
import bisect
input = sys.stdin.readline

meetings = []
N = int(input())
for _ in range(N):
    s, e = tuple((map(int, input().split())))
    bisect.insort_right(meetings, (e, s))

current_time, result = 0, 0
for e, s in meetings:
    if s >= current_time:
        current_time = e
        result += 1

print(result)
