import collections

T = int(input())
for t in range(T):
    line = input()
    stack = collections.deque()
    stopped = False

    for c in line:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stopped = True
                break

    if stopped or len(stack) != 0:
        print("NO")
    else:
        print("YES")