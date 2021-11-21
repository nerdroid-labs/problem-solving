import sys
import collections
def input(): return sys.stdin.readline().rstrip()

N = int(input())
a, b = list(map(int, input().split()))
M = int(input())
graph = collections.defaultdict(list)

for _ in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (N + 1)
queue = collections.deque()
queue.append((a, 0))

ans = -1
while queue:
    person, dist = queue.popleft()

    if person == b:
        ans = dist
        break
    elif visited[person]: continue
    else: visited[person] = True

    for next in graph[person]:
        if not visited[next]:
            queue.append((next, dist + 1))

print(ans)
