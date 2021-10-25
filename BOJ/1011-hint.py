T = int(input())

for t in range(T):
    s, t = map(int, input().split())
    sqrt = round((t - s)**0.5)

    if t - s > sqrt ** 2:
        print(sqrt * 2)
    else:
        print(sqrt * 2 - 1)