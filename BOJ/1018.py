N, M = list(map(int, input().split()))

mat = []
min_colored = float('inf')

for n in range(N):
    line = input()
    mat.append([s for s in line])

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        for start in ("B", "W"):
            cropped = []
            colored = 0

            for s in range(8):
                line = []
                for t in range(8):
                    line.append(mat[i + s][j + t])
                cropped.append(line)

            if cropped[0][0] != start:
                cropped[0][0] = start
                colored += 1

            for s in range(8):
                for t in range(8):
                    if t + 1 < 8 and cropped[s][t] == cropped[s][t+1]:
                        colored += 1
                        if cropped[s][t] == "B":
                            cropped[s][t+1] = "W"

                        elif cropped[s][t] == "W":
                            cropped[s][t+1] = "B"

                    if s + 1 < 8 and cropped[s][t] == cropped[s+1][t]:
                        colored += 1
                        if cropped[s][t] == "B":
                            cropped[s+1][t] = "W"

                        elif cropped[s][t] == "W":
                            cropped[s+1][t] = "B"

            if colored < min_colored:
                min_colored = colored

            # print(*cropped, sep="\n")
            # print()

print(min_colored)