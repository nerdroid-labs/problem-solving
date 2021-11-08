import sys
input = sys.stdin.readline

def recursive(r, c, size, ctr):
    global R, C

    if r == R and c == C:
        print(ctr)
        exit(0)

    next_size = size // 2
    nexts = [(r, c), (r, c + next_size), (r + next_size, c), (r + next_size, c + next_size)]

    for idx in range(4):
        next_r, next_c = nexts[idx]

        if next_r <= R < next_r + next_size and next_c <= C < next_c + next_size:
            recursive(next_r, next_c, next_size, ctr + (next_size ** 2 * idx))


N, R, C = list(map(int, input().split()))
recursive(0, 0, 2**N, 0)
