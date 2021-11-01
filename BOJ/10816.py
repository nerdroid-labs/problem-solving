import collections

ctr = collections.defaultdict(int)
input()
cards = list(map(int, input().split()))
input()
find = list(map(int, input().split()))

for c in cards: ctr[c] += 1
for f in find: print(ctr[f], end=" ")