from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    # 일다능ㄴ 손님이 주문한 단품번호 목록이 있음
    # 최소 2명이상의 손님으로부터 즉,2번이상 주문된 조합을 후보에 포함한다.
    # 그 후보를 return 하는거지>?
    
    
    # 길이
    for c in course:
        all_comb = []
        # 조합 추출
        for order in orders:
            comb = combinations(sorted(order),c)
            all_comb += comb
            
        counter = Counter(all_comb)
        print(counter)

        if counter:
            max_count = counter.most_common(1)[0][1]

            if max_count >= 2:
                for menu, count in counter.items():
                    if count == max_count:
                        answer.append("".join(menu))
    
    return sorted(answer)