import sys
import heapq
import collections

input = sys.stdin.readline

N = int(input())
heap = []
counter = collections.defaultdict(int)

max_ctr = float('-inf')
max_num = 0
total = 0

for i in range(N):
    num = int(input())

    counter[num] += 1
    total += num
    heapq.heappush(heap, num)

max_num = []
max_ctr = float('-inf')

for num in counter:
    if counter[num] > max_ctr:
        max_ctr = counter[num]
        max_num = [num]
    elif counter[num] == max_ctr:
        max_num.append(num)

print(round(total / N))
print(heapq.nsmallest(N // 2 + 1, heap)[-1])
if len(max_num) == 1:
    print(max_num[0])
else:
    print(sorted(max_num)[1])
print(heapq.nlargest(1, heap)[0] - heapq.nsmallest(1, heap)[0])