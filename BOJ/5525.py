import sys
input = sys.stdin.readline


def get_kmp_table(pattern):
    length = len(pattern)
    table = [0] * length

    j = 0
    for i in range(1, length):
        while j > 0 and pattern[j] != pattern[i]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


def kmp(text, pattern):
    n = len(text)
    m = len(pattern)

    ctr = 0
    pi = get_kmp_table(pattern)
    idx = 0

    for i in range(n):
        while idx > 0 and text[i] != pattern[idx]:
            idx = pi[idx - 1]

        if text[i] == pattern[idx]:
            if idx == m - 1:
                ctr += 1
                idx = pi[idx]
            else:
                idx += 1

    return ctr


N = int(input())
input()

PN = "I" + "OI" * N
S = input().rstrip()
print(kmp(S, PN))
