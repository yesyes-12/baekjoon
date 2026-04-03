import heapq
def solution(array, commands):
    lst = []
    for idx in range(len(commands)):
        # print(commands[idx])
        i, j, k = commands[idx]
        
        x = array[i-1:j]
        x_sort = sorted(x)
        # print(x_sort)
        
        lst.append(x_sort[k-1])
        
    return lst
        