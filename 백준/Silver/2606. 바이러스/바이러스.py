def virus():
    n = int(input())
    pair = int(input())

    graph = [[] for _ in range(n + 1)] # 인덱스를 컴퓨터 번호와 맞추기 위해 n + 1개 생성

    for _ in range(pair):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # DFS의 필수
    infected = [False] * (n + 1)

    # DFS 함수 정의
    def dfs(node):
        infected[node] = True # 현재 컴퓨터 감염 처리
        
        # 이웃 컴퓨터들을 하나씩 확인
        for neighbor in graph[node]:
            # 아직 감염되지 않았다면
            if not infected[neighbor]:
                dfs(neighbor) # 감염

    dfs(1)
    print(sum(infected)-1)
virus()