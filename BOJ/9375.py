import sys
import collections
import functools
input = sys.stdin.readline

for _ in range(int(input())):
    clothes = collections.defaultdict(int)

    for __ in range(int(input())):
        _, cloth = input().rstrip().split()
        clothes[cloth] += 1

    print(functools.reduce(lambda y, x: y * (x+1), clothes.values(), 1) - 1)
    