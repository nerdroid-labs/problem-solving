import sys
input = sys.stdin.readline

N, K = list(map(int, input().rstrip().split()))
coins = []

for _ in range(N): coins.append(int(input()))
coins = coins[::-1]

ctr = 0
while K > 0:
    for c in coins:
        if c <= K:
            ctr += K // c
            K %= c
            break

print(ctr)
