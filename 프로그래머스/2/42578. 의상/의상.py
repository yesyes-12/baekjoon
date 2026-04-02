from collections import Counter
def solution(clothes):
    
    type = []
    for i in clothes:
        type.append(i[1])
    
    # 종류만 뽑아 갯수별로 정리
    cnt = Counter(type)
    
    # 종류n+1해서 곱 
    com = 1
    for i in cnt.keys():
        nums = cnt[i] + 1
        com *= nums
    
    return com - 1