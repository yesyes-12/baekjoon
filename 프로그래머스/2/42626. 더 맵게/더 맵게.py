import heapq

def solution(scoville, K):
    # heapq 채우기
    hq = []
    for i in scoville:
        heapq.heappush(hq,i)
    
    count = 0
    while True:
        if (hq[0]>=K):
            break
            
        if (len(hq)==1):
            if (hq[0]<K):
                return -1
        # 1,2위 뽑기
        first = heapq.heappop(hq)
        second = heapq.heappop(hq)
        
        new = first + (second * 2)
        heapq.heappush(hq,new)
        
        count += 1
        
    return count