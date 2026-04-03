from collections import deque
def solution(priorities, location):
    # [2, 1, 3, 2], 2
    queue = deque([(i, prior) for i, prior in enumerate(priorities)])
    
    order = 0
    print(queue)
    
    while queue:
        i, p = queue.popleft()
        
        if any(p < q[1] for q in queue):
            queue.append((i,p))
        else:
            order += 1
            
            if i == location:
                return order