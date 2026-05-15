from collections import deque
def solution(maps):
    answer = 0 # time
    
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    
    n = len(maps)
    m = len(maps[0])
    #print(n,m)
    
    start = None
    end = None
    lever = None
    
    for r, row in enumerate(maps):
        for c, char in enumerate(row):
            if char == "S":
                start = (r,c)
            elif char == "L":
                lever = (r,c)
            elif char == "E":
                end = (r,c)
    print(start, end, lever)
    # bfs
    def bfs(start_r, start_c, target):
        visited = [[False] * m for _ in range(n)]
        visited[start_r][start_c] = True
        
        que = deque([(start_r,start_c,0)])
        
        while que:
            r, c, dist = que.popleft()
            #print(r,c,dist)
            if (r,c) == target:
                return dist
            
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
            
                if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] != "X":
                    if not visited[nr][nc]:
                        if nr == target[0] and nc == target[1]:
                            return dist + 1
                        
                        que.append((nr,nc,dist+1))
                        visited[nr][nc] = True

        return -1
    # S->L
    lvl1 = bfs(start[0], start[1], lever)
    if lvl1 == -1: return -1
    # L->E
    lvl2 = bfs(lever[0], lever[1], end)
    if lvl2 == -1: return -1
    
    return lvl1+lvl2