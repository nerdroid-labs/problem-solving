import sys
import collections
input = sys.stdin.readline


def get_ops(A, B):
    queue = collections.deque()
    queue.append((A, ""))
    visited = [False] * (10000 + 1)

    while queue:
        A, ops = queue.popleft()
        if visited[A]: continue
        else: visited[A] = True
        if A == B: return ops

        A_str = f"{A:04}"
        D = (A * 2) % 10000
        S = (A - 1) % 10000
        L = int(A_str[1:] + A_str[0])
        R = int(A_str[-1] + A_str[:-1])
        if not visited[D]: queue.append((D, ops + "D"))
        if not visited[S]: queue.append((S, ops + "S"))
        if not visited[L]: queue.append((L, ops + "L"))
        if not visited[R]: queue.append((R, ops + "R"))


for _ in range(int(input())):
    A, B = list(map(int, input().rstrip().split()))
    print(get_ops(A, B).strip())
