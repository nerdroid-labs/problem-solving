import sys
import collections
input = sys.stdin.readline

for _ in range(int(input())):
    ops = [char for char in input().rstrip()]
    input()
    line = input().replace("[", "").replace("]", "").rstrip()
    if line == '': nums = collections.deque()
    else: nums = collections.deque(map(int, line.split(',')))
    direction = True
    error = False

    for op in ops:
        if op == "D":
            if not nums:
                error = True
                break
            elif direction:
                nums.popleft()
            else:
                nums.pop()
        elif op == "R":
            direction = not direction

    if error:
        print("error")
    else:
        result = []
        while nums:
            if direction: result.append(str(nums.popleft()))
            else: result.append(str(nums.pop()))

        print(f"[{','.join(result)}]")
