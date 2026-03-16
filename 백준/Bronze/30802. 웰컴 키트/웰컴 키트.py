import sys

input = sys.stdin.readline
def solve():
    N = int(input().strip())
    sizes = list(map(int, input().split()))
    T, P = map(int, input().split())

    tshirts = 0
    for s in sizes:
        if s == 0:
            continue
        tshirts += (s+T-1) // T

    p = N // P
    p_x = N % P

    print(tshirts)
    print(f"{p} {p_x}")

solve()
