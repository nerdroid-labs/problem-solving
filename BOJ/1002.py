T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    center_dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        if min(r1, r2) + center_dist <= max(r1, r2):
            if min(r1, r2) + center_dist < max(r1, r2): print(0)
            else: print(1)
        else:
            if r1 + r2 > center_dist: print(2)
            elif r1 + r2 == center_dist: print(1)
            else: print(0)
