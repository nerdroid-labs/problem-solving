# https://www.youtube.com/watch?v=aPYE0anPZqI

def hanoi(n, frm, left, to):
    global path

    if n == 0: return
    else:
        hanoi(n-1, frm, to, left)
        path.append([frm, to])
        hanoi(n-1, left, frm, to)


path = []
N = int(input())
hanoi(N, 1, 2, 3)

print(len(path))
for s, t in path:
    print(s, t)
