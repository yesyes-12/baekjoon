#10813 공 바꾸기
import sys
N, M = map(int, input().split())
bucket = [ball for ball in range(1,N+1)]
for _ in range(M):
    i,j = map(int, sys.stdin.readline().split())
    f,b = bucket[i-1], bucket[j-1]
    bucket[i-1] = b
    bucket[j-1] = f

for pt in bucket:
    print(pt, end=' ')