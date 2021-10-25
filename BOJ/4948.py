primes = [2]
for i in range(3, 123456 * 2 + 1, 2):
    isPrime = True

    for p in primes:
        if p > i ** 0.5 + 1: break

        elif i % p == 0:
            isPrime = False
            break

    if isPrime: primes.append(i)


while True:
    n = int(input())
    if n == 0: break

    ctr = 0
    for p in primes:
        if n < p <= 2*n:
            ctr += 1

    print(ctr)