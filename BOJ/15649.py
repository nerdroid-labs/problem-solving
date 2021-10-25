import itertools

N, M = list(map(int, input().split()))

for p in itertools.permutations([i for i in range(1, N+1)], M):
    for n in p:
        print(n, end=" ")
    print()