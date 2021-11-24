import sys
import collections
def input(): return sys.stdin.readline().rstrip()


tree = [-1]
depth = [-1]
N = int(input())
for i in range(1, N + 1):
    tree.extend(list(map(int, input().split())))
    depth += [i] * i

length = len(tree)
cache = [float('-inf')] * length
ans = float('-inf')

cache[1] = tree[1]
for i in range(2, length):
    candidate = []
    for parent in (i - (depth[i] - 1) - 1, i - (depth[i] - 1)):
        if 1 <= parent <= length and depth[parent] == depth[i] - 1:
            candidate.append(cache[parent] + tree[i])

    cache[i] = max(candidate)

print(max(cache))
