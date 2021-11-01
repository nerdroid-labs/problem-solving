import math

A, B = list(map(int, input().split()))

gcd = math.gcd(A, B)
mcm = A * B // gcd

print(gcd, mcm)
