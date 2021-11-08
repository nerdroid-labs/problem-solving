import itertools

N = int(input())
M = int(input())

current = 100
if M == 0: brokens = []
else: brokens = list(map(int, input().split()))
possibles = [n for n in range(10) if n not in brokens]
min_diff = float('inf')
closest = float('inf')

for c in range(1, len(str(N)) + 1 + 1):
    for num_set in itertools.product(possibles, repeat=c):
        num = int("".join([str(n) for n in num_set]))

        if min_diff > abs(num - N):
            min_diff = abs(num - N)
            closest = num

only_up_down = abs(current - N)
after_number = len(str(closest)) + abs(closest - N)

print(min(only_up_down, after_number))
