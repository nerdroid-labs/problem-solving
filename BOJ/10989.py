N = int(input())

nums = [0 for x in range(10001)]

for i in range(N):
    nums[int(input())] += 1

for i in range(10001):
    for j in range(nums[i]):
        print(i)