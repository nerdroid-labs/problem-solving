import sys
input = sys.stdin.readline


def recursive(pos, visited, score):
    global steps

    N = len(visited)
    if pos > 0 and visited[pos] and visited[pos - 1]:
        must_skip = True
        key = -pos
    else:
        must_skip = False
        key = pos

    if dp.get(key, float('-inf')) > score:
        return
    else:
        dp[key] = score

    if pos + 1 < N and not must_skip:
        next_visit = visited[:]

        next_visit[pos + 1] = True
        recursive(pos + 1, next_visit, score + steps[pos + 1])

    if pos + 2 < N:
        next_visit = visited[:]
        next_visit[pos + 2] = True

        recursive(pos + 2, next_visit, score + steps[pos + 2])


N = int(input())
steps = []
dp = dict()
for _ in range(N):
    steps.append(int(input()))

recursive(-1, [False for i in range(N)], 0)
print(max(dp.get(N-1, 0), dp.get(-(N-1), 0)))
