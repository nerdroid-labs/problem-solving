N = int(input())

sol = 0
for i in range(1, N):
    origin = i
    parts = [int(s) for s in  str(i)]

    if i + sum(parts) == N:
       sol = i
       break

print(sol)