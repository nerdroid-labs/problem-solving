import collections

line = input()
ops = []
nums = collections.deque()

minus_on = False
for c in line:
    if c == '-': minus_on = True

    if c in ('-', '+'):
        if minus_on:
            ops.append('-')
        else:
            ops.append(c)

for i in line.split("+"):
    for j in i.split("-"):
        nums.append(int(j))

for op in ops:
    x = nums.popleft()
    y = nums.popleft()

    if op == '-':
        nums.appendleft(x - y)
    else:
        nums.appendleft(x + y)

print(*nums)