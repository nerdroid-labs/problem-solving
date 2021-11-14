import sys
input = sys.stdin.readline

M, N = list(map(int, input().split()))
box = []
not_red = 0
reds = []

for r in range(N):
    box.append(list(map(int, input().split())))
    for c in range(M):
        if box[r][c] == 0:
            not_red += 1

        if box[r][c] == 1:
            reds.append((r, c))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
day = 0

while True:
    if not not_red:
        print(day)
        break

    day += 1
    not_red_today = not_red
    will_be_red = set()

    for r, c in reds:
        for i in range(4):
            if 0 <= r + dy[i] < N and 0 <= c + dx[i] < M and not box[r + dy[i]][c + dx[i]]:
                will_be_red.add((r + dy[i], c + dx[i]))

    reds = will_be_red
    for r, c in will_be_red:
        box[r][c] = 1
        not_red -= 1

    if not_red_today == not_red:
        print(-1)
        break
