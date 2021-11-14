import collections
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    existence = collections.defaultdict(bool)
    idx = 0
    max_heap = []
    min_heap = []

    for __ in range(int(input())):

        op, num = input().split()
        num = int(num)

        if op == "I":
            heapq.heappush(max_heap, (-num, idx))
            heapq.heappush(min_heap, (num, idx))
            existence[idx] = True
            idx += 1

        elif op == "D" and max_heap and min_heap:
            if num == 1:
                while max_heap:
                    max_num, max_idx = heapq.heappop(max_heap)
                    if existence[max_idx]:
                        existence.pop(max_idx)
                        break

            else:
                while min_heap:
                    min_num, min_idx = heapq.heappop(min_heap)
                    if existence[min_idx]:
                        existence.pop(min_idx)
                        break

    end_min, end_max = None, None
    while min_heap:
        min_num, min_idx = heapq.heappop(min_heap)
        if existence[min_idx]:
            end_min = min_num
            break

    while max_heap:
        max_num, max_idx = heapq.heappop(max_heap)
        if existence[max_idx]:
            end_max = -max_num
            break

    if not end_min and not end_max:
        print("EMPTY")

    else:
        print(end_max, end_min)
