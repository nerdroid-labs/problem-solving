import sys
input = sys.stdin.readline

K, N = map(int, input().split())
max_len = float('-inf')
max_ans = float('-inf')

lines = []
for k in range(K):
    line = int(input())
    lines.append(line)
    max_len = max(max_len, line)


left = 1
right = max_len
while left <= right:
    mid = (left + right) // 2

    num = 0
    for line in lines:
        num += line // mid

    if num >= N:
        left = mid + 1
        max_ans = max(max_ans, mid)

    else:
        right = mid - 1

print(max_ans)