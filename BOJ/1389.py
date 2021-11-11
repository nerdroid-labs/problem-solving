import sys
import collections
input = sys.stdin.readline

N, M = list(map(int, input().split()))
graph = collections.defaultdict(list)

dist = [[float('inf')] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, t = list(map(int, input().split()))
    dist[s][t] = 1
    dist[t][s] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])

idx = -1
min_val = float('inf')
for i in range(1, N+1):
    dist[i][i] = 0
    total_dist = sum([d for d in dist[i] if d != float('inf')])

    if min_val > total_dist:
        idx = i
        min_val = total_dist

print(idx)
