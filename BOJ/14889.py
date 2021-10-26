import itertools

N = int(input())

advantages = []
for i in range(N):
    advantages.append(list(map(int, input().split())))

diff_min = float('inf')
for A in itertools.combinations(range(N), N // 2):
    B = [x for x in range(N) if x not in A]

    scores = []
    for team in [A, B]:
        score = 0
        for player in team:
            for player_fair in team:
                if player != player_fair:
                    score += advantages[player][player_fair]

        scores.append(score)

    diff = abs(scores[0] - scores[1])
    if diff < diff_min:
        diff_min = diff

print(diff_min)
