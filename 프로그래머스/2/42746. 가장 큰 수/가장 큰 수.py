def solution(numbers):
    chars = sorted(list(map(str, numbers)),reverse=True, key=lambda x : x*3)
    
    if all(x=="0" for x in chars):
        return "0"
    
    big = ""
    for c in chars:
        big+=c
        
    return big
    
    