# 지도는 1x1 크기의 사각형들로 이루어진 직사각형 격자 형태
# 격자의 칸 안에는 'X' 또는 1에서 9 사이의 자연수가 적혀있음.
# X : 바다, 숫자 : 무인도이며 식량을 나타냄.
# 상, 하, 좌, 우로 연결되는 칸에 적힌 숫자를 모두 합한 값은 해당 무인도에서 최대 며칠동안 머물 수 있는지
# maps : 지도
# 각 섬에서 최대 며칠씩 머무를 수 있는지 배열에 오름차순으로 담아 출력
# 만약 지낼 수 있는 무인도가 없다면 -1 출력 

from collections import deque

def bfs(maps, visited, r, c):
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    food = int(maps[r][c])
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in d:
            nr = r + dr
            nc = c + dc
            
            if (0 <= nr < len(maps) and 0 <= nc < len(maps[0])
               and maps[nr][nc].isdigit() and visited[nr][nc] == 0):
                q.append([nr, nc])
                visited[nr][nc] = 1
                food += int(maps[nr][nc])
    
    return food
    
def solution(maps):
    answer = []
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j].isdigit() and visited[i][j] == 0:
                answer.append(bfs(maps, visited, i, j))
            
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)