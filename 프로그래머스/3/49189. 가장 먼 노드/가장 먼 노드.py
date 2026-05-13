from collections import deque
def solution(n, edge):
    # graph 만들기
    graph = {}
    edge.sort()

    for a, b in edge:
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    # bfs
    def bfs(graph, start):
        hubo = 0
        
        que = deque([start])
        visited = [0] * (n+1)
        visited[start] = 1

        while que:
            # 현재 층에 있는 노드 개수
            count = len(que)
            hubo = count

            # 딱 현재 층의 노드만큼만 큐에서 꺼내서 처리
            for _ in range(count):
                cur = que.popleft()
                
                for next_v in graph[cur]:
                    if not visited[next_v]:
                        visited[next_v] = True
                        que.append(next_v)
        return hubo
        
    return bfs(graph,1)