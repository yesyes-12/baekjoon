import sys
input = sys.stdin.readline
def findpw():
    n, m = map(int, input().split())

    info = {}
    for _ in range(n):
        site, pw = input().split()
        info[site] = pw

    for _ in range(m):
        q = input().strip()
        print(info[q])
findpw()