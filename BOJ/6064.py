import sys
import math
input = sys.stdin.readline


def get_cain_digit(num, upper_bound):
    rest = num % upper_bound
    if rest == 0: return upper_bound
    else: return rest


def get_year(x, y, M, N):
    gcd = math.gcd(M, N)
    max_year = (M // gcd) * (N // gcd) * gcd

    if x == 1 and y == 1: return 1
    else:
        isM, isN = False, False
        bigger = max(M, N)

        if M == bigger: isM = True
        else: isN = True

        for q in range(max_year // bigger):
            if isM and get_cain_digit(q * bigger + x % M, N) == y: return q * bigger + x % M
            if isN and get_cain_digit(q * bigger + y % N, M) == x: return q * bigger + y % N

        return -1


for _ in range(int(input())):
    M, N, x, y = list(map(int, input().rstrip().split()))
    print(get_year(x, y, M, N))
