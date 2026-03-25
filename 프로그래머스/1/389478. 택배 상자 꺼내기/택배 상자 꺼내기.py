def solution(n, w, num):
    n-=1
    num-=1
    
    my_row = num // w
    if my_row % 2==0:
        my_col = num % w
    else:
        my_col = (w-1) - num % w
    print(my_row, my_col)
    
    max_row = n // w
    print(max_row)
    
    answer = max_row - my_row
    if max_row % 2 == 0:
        top = max_row * w + my_col
    else:
        top = max_row * w + (w-1-my_col)
    
    if top <= n:
        answer += 1
    return answer