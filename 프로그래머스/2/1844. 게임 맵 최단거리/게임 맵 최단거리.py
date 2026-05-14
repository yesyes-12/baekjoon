from collections import deque
def solution(maps):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False] * m for _ in range(n)]
    
    # 예외 처리
    if maps[0][0] == 0 or maps[n-1][m-1] == 0:
        return -1
    
    que = deque([(0, 0, 1)])
    visited[0][0] = True
    
    # bfs
    while que:
        r, c, dist = que.popleft()
        
        if r == (n-1) and c == (m-1):
            return dist
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if maps[nr][nc] == 1:
                    if not visited[nr][nc]:
                        que.append((nr,nc,dist+1))
                        visited[nr][nc] = True
                        
    return -1