from itertools import permutations
import math
def solution(numbers):
    answer = 0
    
    # 순열 집합
    prime_set = set()

    # 문자열분리해서 순열집합 만들기
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            prime_set.add(num)
    
    # 일단 소수 판별,,
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True         
    
    # 소수만 카운팅
    for i in prime_set:
        if is_prime(i):
            answer+=1
    return answer