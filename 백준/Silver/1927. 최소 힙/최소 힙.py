import sys
import heapq

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    info = int(sys.stdin.readline())
    
    if info == 0:
        print(heapq.heappop(arr)) if arr else print(0)
    else: 
        heapq.heappush(arr, info)