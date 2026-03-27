import sys
from collections import deque
input = sys.stdin.readline


def dfsbfs():
    # 정점 개수, 간선개수, 탐색시작 번호
    n, m, v = map(int, input().split())

    # 재귀 혹은 스택
    def dfs(graph, v, visited):
        # 현재 노드 방문 처리, 출력
        visited[v] = True
        print(v, end=" ")

        # 현재 노드와 연결된 다른 노드 방문
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    # 큐 사용
    def bfs(graph, start, visited):
        # 큐 생성, 시작노드 삽입
        queue = deque([start])
        # 시작노드 방문 처리
        visited[start] = True

        # 큐 빌 때까지 반복
        while queue:
            # 큐에서 원소 뽑기, 출력
            v = queue.popleft()
            print(v, end=" ")

            # 아직 방문하지 않은 인접 원소를 큐에 넣기
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True # 방문중복방지

    graph = [[] for _ in range(n+1)]

    # 간선 입력
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 연결 지점 여러개인 경우를 위해 오름차순 정렬
    for i in range(1, n+1):
        graph[i].sort()

    # 각각 방문 기록 준비
    visited_dfs = [False] * (n+1)
    visited_bfs = [False] * (n+1)

    dfs(graph, v, visited_dfs)
    print()
    bfs(graph, v, visited_bfs)
dfsbfs()
    