from collections import Counter
def solution(nums):
    # nums=[3,1,2,3]
    a = Counter(nums).keys()
    
    answer = 0
    if len(a) > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(a)
    
    return answer