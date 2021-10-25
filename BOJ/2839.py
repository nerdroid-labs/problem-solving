N = int(input())

q_x, q_y = N // 3, N // 5
min_tot = float('inf')

for x in range(q_x + 1):
    if (N - x * 3) % 5 == 0:
        y = (N - x * 3) // 5
        if x+y < min_tot:
            min_tot = x + y

for y in range(q_y + 1):
    if (N - y * 5) % 3 == 0:
        x = (N - y * 5) // 3
        if x+y < min_tot:
            min_tot = x + y

if min_tot == float('inf'):
    min_tot = -1
print(min_tot)