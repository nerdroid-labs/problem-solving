import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N = int(input())
mat = []
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for _ in range(N):
    mat.append([c for c in input().rstrip()])

def dfs(r, c, visit, GR = False):
    visit[r][c] = True
    color = mat[r][c]

    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
            if GR and color in ('G', 'R') and mat[nr][nc] in ('G', 'R'):
                dfs(nr, nc, visit, GR)
            elif mat[nr][nc] == color:
                dfs(nr, nc, visit, GR)


visit_origin = [[False] * N for _ in range(N)]
visit_RG = [[False] * N for _ in range(N)]

region_origin = 0
region_RG = 0

for r in range(N):
    for c in range(N):
        if not visit_origin[r][c]:
            dfs(r, c, visit_origin, False)
            region_origin += 1
        if not visit_RG[r][c]:
            dfs(r, c, visit_RG, True)
            region_RG += 1

print(region_origin, region_RG)
