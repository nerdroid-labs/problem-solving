import sys
def input(): return sys.stdin.readline().rstrip()

dp = dict()
def divide_and_conquer(A, B, C):
    if (A, B) in dp: return dp[(A, B)]

    if B == 1:
        return (A * B) % C
    elif B > 1:
        B_left = B // 2
        B_right = B // 2
        if B % 2 == 1: B_right += 1

        left = divide_and_conquer(A, B_left, C) % C
        right = divide_and_conquer(A, B_right, C) % C
        dp[(A, B)] = (left * right) % C
        return dp[(A, B)]


A, B, C = list(map(int, input().split()))
print(divide_and_conquer(A, B, C))
