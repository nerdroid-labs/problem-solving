import math

MIN, MAX = list(map(int, input().split()))
mark = [True] * (MAX - MIN + 1)

for sqrt in range(2, int(MAX ** 0.5) + 1):
    sq = sqrt ** 2

    for i in range(math.ceil(MIN / sq), math.floor(MAX / sq) + 1):
        mark[sq * i - MIN] = False

print(mark.count(True))

# 1000000000000 1000001000000
# 607940