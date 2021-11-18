import sys
input = sys.stdin.readline

site_password = dict()
N, M = list(map(int, input().rstrip().split()))

for _ in range(N):
    site, password = input().rstrip().split()
    site_password[site] = password

for _ in range(M):
    print(site_password[input().rstrip()])
