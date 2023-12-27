import collections
import sys


def input():
    return sys.stdin.readline()


def get_distance(mbti_1, mbti_2):
    distance = 0

    for i in range(4):
        if mbti_1[i] != mbti_2[i]:
            distance += 1

    return distance


for t in range(int(input())):
    n = int(input())
    cases = sorted(input().split())
    ctr = collections.Counter(cases)

    for mbti in ctr.keys():
        if ctr[mbti] > 3:
            ctr[mbti] = 3

    cases = []
    for mbti, count in ctr.items():
        cases += [mbti] * count

    n = len(cases)
    cache = [[float('inf')] * n for _ in range(n)]
    for s in range(n):
        for t in range(s):
            cache[s][t] = get_distance(cases[s], cases[t])

    answer = float('inf')
    for s in reversed(range(n)):
        for t in reversed(range(s)):
            for k in reversed(range(t)):
                total = cache[s][t] + cache[t][k] + cache[s][k]
                if total <= answer:
                    answer = total

    print(answer)



