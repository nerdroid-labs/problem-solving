import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

hear = set()
see = set()

for _ in range(N): see.add(input().rstrip())
for _ in range(M): hear.add(input().rstrip())

ret = sorted(see & hear)
print(len(ret))
print(*ret, sep="\n")
