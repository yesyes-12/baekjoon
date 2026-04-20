from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length) # 다리 큐
    truck = deque(truck_weights) # 트럭 큐
    current_weight = 0 # 현재 다리 무게
    sec = 0

    while True:
        if (len(truck)==0 and current_weight==0):
            break
            
        sec += 1
        out = bridge.popleft() # 다리에서 나가는 

        if out > 0:
            current_weight -= out
        
        if truck and ((current_weight+truck[0])<=weight):
            bridge.append(truck[0])
            current_weight += truck.popleft()
        else:
            bridge.append(0)
            
    return sec
    