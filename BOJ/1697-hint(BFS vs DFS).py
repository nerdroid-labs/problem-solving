import collections

N, K = list(map(int, input().split()))
queue = collections.deque()
queue.appendleft(N)
MAX = 10 ** 5
depth = [0] * (MAX + 1)

while queue:
    x = queue.popleft()

    if x == K:
        print(depth[x])
        break

    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and depth[nx] == 0:
            queue.append(nx)
            depth[nx] = depth[x] + 1