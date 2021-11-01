import collections
import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == ".": break
    deque = collections.deque()

    is_stopped = True
    remove_other = "".join([s for s in line if s in ("(", ")", "[", "]")])
    for c in remove_other:
        if c in ("[", "("):
            deque.append(c)

        elif c == "]":
            if deque and deque[-1] == "[":
                deque.pop()
            else:
                is_stopped = False
                break

        elif c == ")":
            if deque and deque[-1] == "(":
                deque.pop()
            else:
                is_stopped = False
                break

    if is_stopped and not deque : print("yes")
    else: print("no")