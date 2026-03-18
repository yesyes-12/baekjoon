import sys

input = sys.stdin.readline

def pocketmon_master():
    n, m = map(int, input().split()) # 포켓몬수 # 문제수

    pocketmon = {}
    
    for i in range(1,n+1):
        name = input().strip()
        pocketmon[i] = name
    
    pocketmon_reverse={v:k for k,v in pocketmon.items()}

    for _ in range(m):
        guess = input().strip()
        if guess.isnumeric():
            print(pocketmon[int(guess)])
        else:
            print(pocketmon_reverse[guess])

pocketmon_master()