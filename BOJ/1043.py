import sys
import collections
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
know = set(list(map(int, input().split()))[1:])
graph = collections.defaultdict(list)
visit = [False] * (100 + 1)
party = []

for n in range(M):
    attendees = list(map(int, input().split()))[1:]
    party.append(set(attendees))

    for at in attendees:
        graph[n + 51].append(at)
        graph[at].append(n + 51)


def bfs(node):
    if not graph[node]:
        return []
    else:
        group = []
        for next_node in graph[node]:
            if not visit[next_node]:
                visit[next_node] = True
                if next_node < 51:
                    group.append(next_node)
                group.extend(bfs(next_node))
        return group


candidates = []
for n in range(100 + 1):
    if not visit[n]:
        ret = bfs(n)
        if ret: candidates.append(set(ret))

exception_set = set()
for candidate in candidates:
    if candidate & know: exception_set |= candidate

ctr = 0
for p in party:
    if not p & exception_set: ctr += 1

print(ctr)
