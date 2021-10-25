N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))

sol = float('-inf')
for card1 in range(N):
    for card2 in range(N):
        for card3 in range(N):
            candidate = [card1, card2, card3]
            if len(candidate) != len(set(candidate)):
                continue
            else:
                candidate = [cards[card1], cards[card2], cards[card3]]
                sub_sol = sum(candidate)
                if sub_sol <= M and M - sub_sol < M - sol:
                    sol = sub_sol

print(sol)