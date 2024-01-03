#11021 A+B - 7
import sys
T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    n = a + b
    print(f"Case #{i+1}: {n}")