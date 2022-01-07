import itertools

N, M = list(map(int, input().split()))

for prod in itertools.product(*[[i for i in range(1, N+1)] for matrix in range(M)]):
    for n in prod:
        print(n, end=" ")
    print()