N = int(input())

fact = 1
for i in range(1, N+1): fact *= i

print(len(str(fact)) - len(str(fact).rstrip("0")))
