import collections

min_ans = float('inf')
max_ans = float('-inf')


def recursive(ops, nums: collections.deque):
    global min_ans, max_ans
    if len(nums) == 1:
        if min_ans > nums[0]: min_ans = nums[0]
        if max_ans < nums[0]: max_ans = nums[0]
        return

    for op in range(4):
        if ops[op] > 0:
            o1 = nums.popleft()
            o2 = nums.popleft()

            if op == 0: nums.appendleft(o1 + o2)
            elif op == 1: nums.appendleft(o1 - o2)
            elif op == 2: nums.appendleft(o1 * o2)
            elif op == 3:
                if o1 < 0 and o2 > 0:
                    nums.appendleft(-(-o1 // o2))
                else:
                    nums.appendleft(o1 // o2)

            ops[op] -= 1
            recursive(ops, nums)

            ops[op] += 1
            nums.popleft()
            nums.appendleft(o2)
            nums.appendleft(o1)


input()
nums = collections.deque(map(int, input().split()))
ops = list(map(int, input().split()))
recursive(ops, nums)

print(max_ans)
print(min_ans)