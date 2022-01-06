import sys


def input():
	return sys.stdin.readline().rstrip()


N = int(input())
points = []

for _ in range(N):
	points.append(list(map(int, input().split())))

answer = 0
points += [points[0]]

for i in range(N):
	answer += points[i][0] * points[i + 1][1] - points[i + 1][0] * points[i][1]

print(round(abs(answer)/2, 1))
