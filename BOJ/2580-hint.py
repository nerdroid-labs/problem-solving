import sys
import collections


def sudoku(coords, rows, cols, sections):
    global matrix

    if not coords:
        for m in matrix:
            print(" ".join(list(map(str, m))))
        exit(0)

    for n in range(1, 10):
        r, c = coords[-1]
        section_r, section_c = r // 3, c // 3
        if not rows[r][n] and not cols[c][n] and not sections[section_r][section_c][n]:
            matrix[r][c] = n
            rows[r][n] = True
            cols[c][n] = True
            sections[section_r][section_c][n] = True

            sudoku(coords[:len(coords) - 1], rows, cols, sections)

            matrix[r][c] = 0
            rows[r][n] = False
            cols[c][n] = False
            sections[section_r][section_c][n] = False


matrix = []
coords = collections.deque()
rows = [[False for i in range(10)] for j in range(9)]
cols = [[False for i in range(10)] for j in range(9)]
sections = [[[False for t in range(10)] for j in range(3)] for i in range(3)]

for r in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    for i, e in enumerate(line):
        if e == 0:
            coords.append([r, i])
        else:
            rows[r][e] = True
            cols[i][e] = True
            section_r, section_c = r // 3, i // 3
            sections[section_r][section_c][e] = True

    matrix.append(line)

sudoku(coords, rows, cols, sections)