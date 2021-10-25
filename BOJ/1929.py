M, N = map(int, input().split())

primes = [2]
for i in range(3, N + 1, 2):
    isPrime = True

    for p in primes:
        if p > i ** 0.5 + 1: break

        elif i % p == 0:
            isPrime = False
            break

    if isPrime: primes.append(i)

for p in primes:
    if M <= p <= N:
        print(p)