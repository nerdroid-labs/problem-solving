import sys
input = sys.stdin.readline


M, N, H = list(map(int, input().rstrip().split()))
box = []
not_red = 0
reds = set()

for h in range(H):
    floor = []
    for r in range(N):
        line = list(map(int, input().rstrip().split()))
        floor.append(line)

        for c in range(M):
            if line[c] == 0: not_red += 1
            elif line[c] == 1: reds.add((h, r, c))

    box.append(floor)

dh = [0,0,0,0,1,-1]
dr = [0,0,1,-1,0,0]
dc = [1,-1,0,0,0,0]
day = 0

while not_red > 0:
    day += 1
    reds_next_day = set()

    for h, r, c in reds:
        for i in range(6):
            if 0 <= h + dh[i] < H and 0 <= r + dr[i] < N and 0 <= c + dc[i] < M and box[h + dh[i]][r + dr[i]][c + dc[i]] == 0:
                reds_next_day.add((h + dh[i], r + dr[i], c + dc[i]))

    if not reds_next_day:
        print(-1)
        exit(0)

    else:
        for h, r, c in reds_next_day:
            box[h][r][c] = 1
            not_red -= 1

        reds = reds_next_day

print(day)
