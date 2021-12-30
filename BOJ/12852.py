import collections
import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
parent = [i for i in range(N + 1)]
dp = [sys.maxsize] * (N + 1)

queue = collections.deque()
queue.append((N, 0, 0))

while queue:
	num, frm, ctr = queue.popleft()

	if dp[num] > ctr:
		dp[num] = ctr
		parent[num] = frm
	else:
		continue

	if num % 3 == 0:
		queue.append((num // 3, num, ctr + 1))

	if num % 2 == 0:
		queue.append((num // 2, num, ctr + 1))

	if num - 1 >= 1:
		queue.append((num - 1, num, ctr + 1))

print(dp[1])

path = []
current = 1
while current != N:
	path.append(current)
	current = parent[current]
path.append(N)
path.reverse()

print(*path, sep=" ")
