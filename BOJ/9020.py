primes = [2]
for i in range(3, 10001, 2):
    isPrime = True

    for p in primes:
        if p > i ** 0.5 + 1: break

        elif i % p == 0:
            isPrime = False
            break

    if isPrime: primes.append(i)


T = int(input())

for t in range(T):
    n = int(input())

    p_1, p_2 = float('inf'), float('-inf')

    for p in primes:
        if n - p in primes and abs(p_1 - p_2) > abs(n - p - p):
            p_1 = min([n - p, p])
            p_2 = max([n - p, p])
    
    print(p_1, p_2)