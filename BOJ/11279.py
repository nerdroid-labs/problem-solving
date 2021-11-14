import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    op = int(input())

    if op == 0:
        if heap: print(heapq.heappop(heap)[1])
        else: print(0)
    else:
        heapq.heappush(heap, (-op, op))
