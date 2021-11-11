import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
from_index = []
from_name = dict()

for _ in range(N):
    line = input().rstrip()
    from_index.append(line)
    from_name[line] = len(from_index)

for _ in range(M):
    line = input().rstrip()

    if line.isalpha():
        print(from_name[line])
    else:
        print(from_index[int(line) - 1])
