import sys
import collections
import heapq
def input(): return sys.stdin.readline().rstrip()

N = int(input())
sea = []
shark_r, shark_c = -1, -1
for r in range(N):
    sea.append(list(map(int, input().split())))

for r in range(N):
    for c in range(N):
        if sea[r][c] == 9:
            shark_r, shark_c = r, c

day = 0
eat = 0
size = 2
visit_for_reset = [[False] * N for _ in range(N)]
visit = [v[:] for v in visit_for_reset]

heap = []
heapq.heappush(heap, (0, shark_r, shark_c))
sea[shark_r][shark_c] = 0

while heap:
    dist, r, c = heapq.heappop(heap)

    if visit[r][c]: continue
    else: visit[r][c] = True

    if 0 < sea[r][c] < size:
        eat += 1
        day += dist

        if eat == size:
            eat = 0
            size += 1

        dist = 0
        sea[r][c] = 0
        visit = [v[:] for v in visit_for_reset]
        heap = []

    for dr, dc in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and sea[nr][nc] <= size:
            heapq.heappush(heap, (dist + 1, nr, nc))

print(day)
