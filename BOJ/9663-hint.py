N = int(input())
ans = 0

def queen(visited):
    global N, ans

    n = len(visited)
    if n == N:
        ans += 1
        # print(visited)
        return

    r = n + 1
    for c in range(1, N+1):
        flag = True
        for last_r, last_c in visited:
            if last_c == c or last_r == r or (abs(last_r - r) == abs(last_c - c)):
                flag = False
                break

        if flag:
            visited.append((r, c))
            queen(visited)
            visited.pop()


for c_init in range(1, N+1):
    queen(visited=[(1, c_init)])

print(ans)