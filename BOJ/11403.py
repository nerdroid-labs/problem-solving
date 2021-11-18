import sys
import collections
input = sys.stdin.readline

mat = []
N = int(input())
for _ in range(N):
    mat.append(list(map(int, input().rstrip().split())))

path = [["0"] * N for _ in range(N)]
for s in range(N):
    visit = [False] * N
    queue = collections.deque()
    queue.append(s)

    while queue:
        node = queue.popleft()
        if visit[node]: continue
        else: visit[node] = True

        for i in range(N):
            if mat[node][i] == 1:
                path[s][i] = "1"
                if not visit[i]: queue.append(i)

for p in path: print(" ".join(p))
