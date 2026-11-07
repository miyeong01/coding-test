# 직사각형 격자 형태의 미로
# 통로만 이동할 수 있음.
# 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 레버를 당겨서만 열 수 있음. 
# 레버 또한 통로들 중 한 칸에 있음.
# 출발 지점 -> 레버 -> 출구
# 한 칸 이동할 때 1초가 걸릴 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간 구하기 
# S : 시작 지점, E : 출구, L : 레버 
# O : 통로, X : 벽 

from collections import deque

def bfs(maps, start, target):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    d = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    q = deque()
    q.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = 1
    
    while q:
        r, c, time = q.popleft()
        
        if maps[r][c] == target:
            return time
        
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            
            if ((0 <= nr < len(maps)) and (0 <= nc < len(maps[0]))
            and maps[nr][nc] != "X" and visited[nr][nc] == 0):
                visited[nr][nc] = 1
                q.append([nr, nc, time + 1])
    
    return -1
                

def solution(maps):
    answer = 0
    start = [0, 0]
    lever = [0, 0]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
                
    time1 = bfs(maps, start, "L")
    time2 = bfs(maps, lever, "E")
    
    if time1 == -1 or time2 == -1:
        return -1
    else:
        return time1 + time2