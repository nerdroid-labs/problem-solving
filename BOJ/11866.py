import collections

N, K = list(map(int, input().split()))

nums = collections.deque([i for i in range(1, N+1)])
ret = []

while len(ret) < N:
    nums.rotate(-(K-1))
    ret.append(nums.popleft())

print(f"<{', '.join([str(r) for r in ret])}>")
