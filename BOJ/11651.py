N = int(input())

group = []
for i in range(N):
    group.append(list(map(int, input().split())))

group.sort(key=lambda x: (x[1], x[0]))

for x, y in group:
    print(x, y)