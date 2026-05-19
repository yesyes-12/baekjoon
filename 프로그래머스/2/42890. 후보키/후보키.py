from itertools import combinations
def solution(relation):
    r = len(relation)
    c = len(relation[0])
    
    candidates = []
    for i in range(1, c+1):
        candidates.extend(combinations(range(c),i))
        
    final_candidates = []
    
    for candi in candidates:
        row_tup = []
        for row in relation:
            tup = tuple(row[c] for c in candi)
            row_tup.append(tup)
        
        if len(set(row_tup)) == r:
            is_minimal = True
            for key in final_candidates:
                if set(key).issubset(set(candi)):
                    is_minimal = False
                    break
            
            if is_minimal:
                final_candidates.append(candi)
                
                
    return len(final_candidates)