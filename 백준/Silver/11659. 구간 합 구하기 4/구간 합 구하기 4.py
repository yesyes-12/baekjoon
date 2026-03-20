import sys
input = sys.stdin.readline
def periodSum():
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    pr_sum = [0]
    temp = 0

    for num in numbers:
        temp += num
        pr_sum.append(temp)
        
    for _ in range(m):
        i,j = map(int, input().split())
        print(pr_sum[j]-pr_sum[i-1])
periodSum()