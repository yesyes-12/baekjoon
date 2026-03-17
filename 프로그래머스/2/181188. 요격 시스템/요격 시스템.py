def solution(targets):
    targets.sort(key=lambda x: x[1]) # 정렬 끝점기준

    last_intercept = 0 # 끝점 시작
    missile = 0 
    for s, e in targets: 
        if s >= last_intercept: # 공격미사일 시작점이 마지막 요격미사일 지점보다 크거나 같으면
            last_intercept = e # 갱신
            missile += 1
        
    return missile