N = int(input())
data = []
ranks = []

for n in range(N):
    data.append(list(map(int, input().split())))

for d_ori in range(N):
    rank = 1

    for d_cmp in range(N):
        if d_cmp == d_ori: continue

        ori_x, ori_y = data[d_ori]
        cmp_x, cmp_y = data[d_cmp]

        if ori_x < cmp_x and ori_y < cmp_y:
            rank += 1

    ranks.append(str(rank))

print(" ".join(ranks))