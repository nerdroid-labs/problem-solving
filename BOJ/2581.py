primes = [2]
for i in range(3, 10001, 2):
    isPrime = True

    for p in primes:
        if i % p == 0:
            isPrime = False
            break

    if isPrime: primes.append(i)

M = int(input())
N = int(input())

total = 0
min_prime = float('inf')
for n in range(M, N+1):
    if n in primes:
        total += n
        if n < min_prime: min_prime = n

if min_prime == float('inf') : print(-1)
else :
    print(total)
    print(min_prime)