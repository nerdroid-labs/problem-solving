def get_matrix(N, M):
	return [[M * r + c for c in range(1, M + 1)] for r in range(N)]


def clock_wise(matrix):
	ret = [list(line) for line in zip(*matrix[::-1])]
	return ret


def counter_clock_wise(matrix):
	ret = [list(line) for line in zip(*matrix)]
	ret.reverse()
	return ret


def flip_vertically(matrix):
	return matrix[::-1]


def flip_horizontally(matrix):
	return [line[::-1] for line in matrix]


def print_matrix(matrix):
	print(*matrix, sep="\n", end="\n\n")


matrix = get_matrix(3, 4)
print("[Original]")
print_matrix(matrix)

clock = clock_wise(matrix)
print("[Rotated] Clock wise")
print_matrix(clock)

counter_clock = counter_clock_wise(matrix)
print("[Rotated] Counter clock wise")
print_matrix(counter_clock)

vertical = flip_vertically(matrix)
print("[Flipped] Vertically")
print_matrix(vertical)

horizontal = flip_horizontally(matrix)
print("[Flipped] horizontally")
print_matrix(horizontal)
