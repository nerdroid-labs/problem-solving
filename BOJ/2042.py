import sys
def input(): return sys.stdin.readline().rstrip()

N, M, K = list(map(int, input().split()))
nums = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)


def init(node, start, end):
	if start == end:
		tree[node] = nums[start]
		return tree[node]
	else:
		tree[node] = init(node * 2, start, (start+end) // 2) + init(node*2 + 1, (start + end)//2 + 1, end)
		return tree[node]


# node: 현재 노드
# start: 현재 노드가 가리키는 시작 인덱스, end: 현재 노드가 가리키는 끝 인덱스
# index: 구간 합을 수정하고자 하는 노드
# diff: 수정할 값
def update(node, start, end, index, diff):
	if index < start or index > end:
		return

	tree[node] += diff

	if start != end:
		update(node*2, start, (start+end) // 2, index, diff)
		update(node*2+1, (start+end)//2 + 1, end, index, diff)


# node: 현재 노드
# start: 현재 노드가 가리키는 시작 인덱스, end: 현재 노드가 가리키는 끝 인덱스
# left: 찾을 범위의 시작점, right: 찾을 범위의 끝점
def query(node, start, end, left, right):
	if left > end or right < start:
		return 0

	if left <= start and end <= right:
		return tree[node]

	return query(node*2, start, (start+end)//2, left, right) + query(node*2+1, (start+end)//2+1, end, left, right)


init(1, 0, N - 1)
for _ in range(M + K):
	a, b, c = list(map(int, input().split()))

	if a == 1:
		diff = c - nums[b - 1]
		nums[b - 1] = c
		update(1, 0, N - 1, b - 1, diff)
	elif a == 2:
		print(query(1, 0, N - 1, b - 1, c - 1))
