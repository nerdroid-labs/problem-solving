N, M = list(map(int, input().split()))
heights = list(map(int, input().split()))

left, right = 0, max(heights)
best = float('-inf')

while left <= right:
    mid = (left + right) // 2
    cuts = [h - mid for h in heights if h > mid]

    if sum(cuts) < M:
        right = mid - 1

    elif sum(cuts) >= M:
        left = mid + 1
        if mid > best:
            best = mid

print(best)