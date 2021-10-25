N = int(input())
primes = []

while N > 1 :
    for i in range(2, N+1):
        if N % i == 0:
            N //= i
            primes.append(i)
            break

print(*primes, sep="\n") 