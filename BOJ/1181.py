N = int(input())

words = []
for i in range(N):
    word = input().strip()

    if word not in words:
        words.append(word)

words.sort(key=lambda x: (len(x), x))
print(*words, sep="\n")