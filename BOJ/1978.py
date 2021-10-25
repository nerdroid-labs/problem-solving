input()
nums = map(int, input().split())

primes = [2]
for i in range(3, 1001):
    isPrime = True

    for p in primes:
        if i % p == 0:
            isPrime = False
            break

    if isPrime: primes.append(i)

ans = 0
for n in nums:
    if n in primes: ans += 1

print(ans)