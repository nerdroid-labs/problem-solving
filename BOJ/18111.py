import sys
input = sys.stdin.readline

N, M, B = list(map(int, input().split()))
area = N * M
ground = []

best_time = float('inf')
best_height = float('-inf')

for n in range(N):
    ground.extend(list(map(int, input().split())))

total_block = sum(ground) + B
max_height = min(total_block // area, 256)

for height in range(max_height + 1):
    time = 0

    for g in ground:
        if g < height: time += height - g
        else: time += (g - height) * 2

    if time < best_time:
        best_time = time
        best_height = height

    elif time == best_time:
        if height > best_height:
            best_height = height

print(best_time, best_height)

3