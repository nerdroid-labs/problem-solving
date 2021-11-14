import sys
input = sys.stdin.readline

input()
works = list(map(int, input().split()))
works.sort()
time = 0
sub_total = 0

for w in works:
    sub_total += w
    time += sub_total

print(time)
