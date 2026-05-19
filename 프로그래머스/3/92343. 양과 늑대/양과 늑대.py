from collections import deque, defaultdict
def solution(info, edges):
    answer = 0
    
    # 일단 트리/그래프 만들기
    tree = defaultdict(list)
    for a,b in edges:
        tree[a].append(b)

    # dfs
    def dfs(curr, sheep, wolves, next_nodes):
        if curr == 0:
            sheep += 1
            
        # if 늑대>=양 return
        if wolves>=sheep:
            return
        # 양의 수 비교
        nonlocal answer
        answer = max(answer, sheep)
        
        # 방금 방문한 노드는 목록에서 지우고 노드의 자식들 추가
        new_v = [v for v in next_nodes if v != curr] + tree[curr]
        
        for nv in new_v:
            # next
            if info[nv] == 0: # 양
                dfs(nv, sheep+1, wolves, new_v)
            else: # 늑대
                dfs(nv, sheep, wolves+1, new_v)
                
    dfs(0, 0, 0, [0])
    
    return answer