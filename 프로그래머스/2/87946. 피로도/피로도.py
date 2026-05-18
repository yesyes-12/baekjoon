from itertools import permutations
def solution(k, dungeons):
    answer = -1
     # 탐험시작위한 최소필요 피로도
    # 마쳤을때 소모피로도'
    
    # solution(k: int, dungeons: List[List[int]]) -> int
    course = [list(p) for p in permutations(dungeons)]
    # 순열 완탐
    for path in course:
        #print(f"던전순서: {path}")
        clear = 0 # 던전 클리어 수
        crt_k = k # k
        #print(f"클리어수: {clear},{crt_k}")
        for piro in path:
            if crt_k >= piro[0]:
                crt_k -= piro[1]
                clear += 1
            if clear > answer:
                answer = clear
            #print(f"클리어수: {clear},{crt_k}")
        
    return answer