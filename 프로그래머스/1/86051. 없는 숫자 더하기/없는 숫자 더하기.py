def solution(numbers):
    correct = set([0,1,2,3,4,5,6,7,8,9])
    numbers = set(numbers)
    
    answer = sum(correct-numbers)
    
        
    return answer