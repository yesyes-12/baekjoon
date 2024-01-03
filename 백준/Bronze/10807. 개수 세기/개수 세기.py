#10807 개수 세기
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
f = int(input())
print(data.count(f))