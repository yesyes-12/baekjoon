from collections import defaultdict, deque
def solution(n, wires):
    answer = n
    
    # wires 이용해 인접 리스트dict 만들기
    tree = defaultdict(list)
    
    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)

    # bfs
    def bfs(start, graph, n):
        
        q = deque([start])
        visited = [False] * (n+1)
        
        visited[start] = True
        cnt = 1
        
        while q:
            cuv = q.popleft()
            
            for nv in graph[cuv]:
                if not visited[nv]:
                    q.append(nv)
                    visited[nv] = True
                    cnt+=1
        return cnt
    
    # wires 순회하며 v1 <-> v2의 연결 임시로 끊기
    for v1, v2 in wires:
        tree[v1].remove(v2)
        tree[v2].remove(v1)
        # v1 시작점, bfs
        # 연결된 노드 개수 count
        cnt = bfs(v1, tree, n)
        
        # 개수 비교
        answer = min(answer, abs(2*cnt-n))

        # 끊었던 v1 <-> v2 다시 연결
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    return answer