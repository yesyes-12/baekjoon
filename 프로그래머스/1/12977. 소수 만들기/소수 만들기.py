from itertools import combinations
import math

def solution(nums):
    answer = 0
    
    # 세개 뽑기? 조합?
    combs = list(combinations(nums,3))
    # 소수 판별 isprime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    for i in combs:
        summ = sum(i)
        if is_prime(summ):
            # 카운팅 하기
            answer += 1
        
    return answer