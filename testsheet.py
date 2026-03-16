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


def ISBN():
    isbn = input().strip()

    weight = [1,3,1,3,1,3,1,3,1,3,1,3,1]

    for x in range(10):
        sum = 0
        for i in range(13):
            if isbn[i] == "*":
                sum += x * weight[i]
            else:
                sum += int(isbn[i]) * weight[i]

        if sum % 10 == 0:
            print(x)
            break

def FizzBuzz():
    strings = [ input().strip() for _ in range(3)]

    n = 0
    for i in range(3):
        if strings[i].isdigit():
            n = int(strings[i]) + (3-i)
            break

    if (n % 3 == 0) and (n % 5 ==0):
        print("FizzBuzz")
    elif (n % 3 == 0) and not (n % 5 == 0):
        print("Fizz")
    elif not (n % 3 == 0) and (n % 5 ==0):
        print("Buzz")
    else:
        print(n)

def make1():
    n = int(input().strip())

    dp = [0] * (n+1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

    print(dp[n])

def PEkit(n=2, lost=[], reserve=[]):
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)

    real_lost = sorted(list(real_lost))

    for i in real_lost:
        if i-1 in real_reserve:
            real_lost.remove(i-1)
        elif i+1 in real_reserve:
            real_lost.remove(i+1)
        else:
            n -= 1
    
    return n
PEkit(5,[2,4])