import sys

input = sys.stdin.readline

def coin0():
    n, k = map(int, input().split())

    coins = [int(input()) for _ in range(n)]

    num = 0
    for coin in reversed(coins):
        if k == 0:
            break
            
        if coin <= k:
            num += k // coin
            # 남은 금액은 '나머지'로 한 번에 갱신
            k %= coin
    print(num)
coin0()