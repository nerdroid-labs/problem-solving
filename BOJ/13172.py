import math
import sys


def input():
	return sys.stdin.readline().rstrip()


def extended_gcd(a, b):
	x0, x1, y0, y1 = 1, 0, 0, 1

	while b != 0:
		n, a, b = a // b, b, a % b
		x0, x1 = x1, x0 - n * x1
		y0, y1 = y1, y0 - n * y1

	return x0, y0


N = int(input())
down, up = list(map(int, input().split()))

for _ in range(N - 1):
	d, u = list(map(int, input().split()))
	gcd = math.gcd(d, down)
	lcm = (d // gcd) * (down // gcd) * gcd

	up = u * (lcm // d) + up * (lcm // down)
	down = lcm

div = 1000000007
x, y = extended_gcd(down, div)
print(up * x % div)
