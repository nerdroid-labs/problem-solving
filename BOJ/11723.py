import sys
input = sys.stdin.readline

S = [False for i in range(20 + 1)]
S_empty = [False for i in range(20 + 1)]
S_all = [True for i in range(20 + 1)]
for _ in range(int(input())):
    line = input().split()
    if len(line) == 2:
        op, x = line
        x = int(x)
    else:
        op = line[0]

    if op == "add": S[x] = True
    elif op == "remove": S[x] = False
    elif op == "check": print(int(S[x]))
    elif op == "toggle": S[x] = not S[x]
    elif op == "all": S = S_all[:]
    elif op == "empty": S = S_empty[:]
