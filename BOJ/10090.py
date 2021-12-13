import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
nums = list(map(int, input().split()))


def merge(low_arr, high_arr):
	global ctr

	l_i, h_i = 0, 0
	merged_list = []
	while l_i < len(low_arr) and h_i < len(high_arr):
		if low_arr[l_i] <= high_arr[h_i]:
			merged_list.append(low_arr[l_i])
			l_i += 1
		else:
			merged_list.append(high_arr[h_i])
			h_i += 1
			ctr += len(low_arr) - l_i

	while l_i < len(low_arr):
		merged_list.append(low_arr[l_i])
		l_i += 1

	while h_i < len(high_arr):
		merged_list.append(high_arr[h_i])
		h_i += 1

	return merged_list


def merge_sort(arr):
	length = len(arr)

	if length < 2:
		return arr

	mid = length // 2
	low_arr = merge_sort(arr[:mid])
	high_arr = merge_sort(arr[mid:])

	return merge(low_arr, high_arr)


ctr = 0
merge_sort(nums)
print(ctr)
