# 쉬운 최단거리
from collections import deque

n,m = map(int,input().split())
arr = []
visited = [ [ -1 for i in range(m)] for j in range(n)]

dx = [0,-1,0,1]
dy = [1,0,-1,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 0

    while queue:
        x,y = queue.popleft()

        for t in range(4):
            nx, ny = dx[t] + x, dy[t] + y

            if 0 <= nx < n and 0<= ny < m and visited[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))

for i in range(n):
    temp = list(map(int,input().split()))
    arr.append(temp)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()