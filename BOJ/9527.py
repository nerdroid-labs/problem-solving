import sys


# ctr은 0 ~ N 까지의 f(x)의 합을 반환한다.
# ctr(12)의 경우, 0 ~ 1110에 대해 f(x)의 합을 반환한다.
# 이 경우에 최장 길이인 네자리 이진수에 해당 하는 경우와 그렇지 않은 경우로 나누어 계산할 수 있다.
# 즉, 1000 ~ 1110과 0 ~ 111으로 나누어 계산할 수 있다.
# 1. [1000 ~ 1110] 4번째 자리에 해당 하는 1은 (1)000 ~ (1)110이므로 110 + 1개
# 2. [1000 ~ 1110] 4번째 자리를 제외한 000 ~ 110에는 1이 몇개 있을까? -> ctr(6)과 동일
# 3. [0 ~ 111] 0 ~ 0111은 부분은 공식으로 구할 수 있음
# * 000 ~ 111까지 2 ** 3개의 숫자가 존재.
# * 각 숫자는 3개의 0과 1로 이루어지므로, 총 0과 1이 3 * (2 ** 3)개 존재.
# * 0의 갯수와 1의 갯수는 동일하므로 3 * (2 ** 3) // 2가 1의 숫자.
# * 일반화 하면, N * (2 ** N) // 2 혹은 N * (2 ** N - 1).
# 결론적으로, 1 ~ 3의 결과를 합하면 문제를 해결할 수 있음.
def ctr(N):
	if N == 0:
		return 0
	elif N == 1:
		return 1

	l = len(bin(N)) - 2
	ones_on_lth = N - 2 ** (l - 1) + 1
	ones_after_lth = ctr(N - 2 ** (l - 1))
	ones_when_lth_is_zero = (l - 1) * 2 ** (l - 2)

	return ones_on_lth + ones_after_lth + ones_when_lth_is_zero


def input():
	return sys.stdin.readline().rstrip()


A, B = list(map(int, input().split()))
print(ctr(B) - ctr(A - 1))
