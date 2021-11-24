import sys
import functools
def input(): return sys.stdin.readline().rstrip()

N, M = list(map(int, input().split()))
M = min(M, N - M)

top = functools.reduce(lambda x, y: x * y, [N - i for i in range(M)], 1)
bottom = functools.reduce(lambda x, y: x * y, [i for i in range(1, M + 1)], 1)
print(top // bottom)
