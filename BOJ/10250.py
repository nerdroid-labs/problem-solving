T = int(input())

for t in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        print(f"{H}{N // H:02}")
    else:
        print(f"{N % H}{N // H + 1:02}")