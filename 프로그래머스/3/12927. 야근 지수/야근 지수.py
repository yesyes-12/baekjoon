import heapq
def solution(n,works):
    if sum(works) <= n:
        return 0
    
    heap_reverse = [-w for w in works]
    heapq.heapify(heap_reverse)

    for i in range(n):
        max_work = heapq.heappop(heap_reverse)
        max_work+=1
        heapq.heappush(heap_reverse, max_work)

    anw = 0
    for i in heap_reverse:
        anw += i**2
    
    return anw