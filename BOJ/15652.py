def backtracking(group, seq, M):
    if len(group) == M:
        for g in group:
            print(g, end=" ")

        print()

    else:
        for s in seq:
            if len(group) == 0 or group[-1] <= s:
                next = group.copy()
                next.append(s)
                backtracking(next, seq, M)


N, M = list(map(int, input().split()))
sequence = [i for i in range(1, N+1)]
backtracking([], sequence, M)