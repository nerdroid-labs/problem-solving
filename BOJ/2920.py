des = False
asc = False

nums = list(map(int, input().split()))

for i in range(0, len(nums) - 1):
    if nums[i] < nums[i+1]:
        asc = True

    if nums[i] > nums[i+1]:
        des = True

if asc and des:
    print("mixed")
elif asc:
    print("ascending")
else:
    print("descending")