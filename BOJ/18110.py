import math


def up(num):
    return math.floor(num + 0.5)


N = int(input())
cut = up(N * 0.15)
rates = sorted([int(input()) for _ in range(N)])
rates = [rates[idx] for idx in range(cut, len(rates) - cut)]

if not rates:
    print(0)
else:
    print(up(sum(rates)/len(rates)))
