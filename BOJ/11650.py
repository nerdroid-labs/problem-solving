N = int(input())

group = []
for i in range(N):
    group.append(list(map(int, input().split())))

group.sort()

for x, y in group:
    print(x, y)