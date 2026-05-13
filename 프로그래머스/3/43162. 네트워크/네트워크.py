def solution(n, computers):
    answer = 0
    # 방문 여부
    visited = [0] * n
    # dfs
    def dfs(node):
        # 방문
        visited[node] = 1
        for next_node in range(n):
            # 나 빼고 연결되어 있는 노드, 방문 x
            if computers[node][next_node] == 1 and not visited[next_node]:
                dfs(next_node)
                
    for i in range(n):
        if visited[i]:
            continue
        dfs(i)
        answer+=1
    return answer