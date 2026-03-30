from collections import Counter
def solution(participant, completion):
    # 참여선수, 완주선수 배열
    part = Counter(participant)
    comple = Counter(completion)
    
    non = list((part - comple).keys())
    
    return non[0]