import itertools

N, M = list(map(int, input().split()))

for comb in itertools([i for i in range(1, N+1)], M):
    for n in comb:
        print(n, end=" ")
    print()