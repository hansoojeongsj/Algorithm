from collections import deque

# 입력 받기
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # 정점 번호가 1번부터 시작

# 간선 정보 저장 (양방향)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서 정렬을 위해 오름차순 정렬
for edges in graph:
    edges.sort()

# DFS 함수 (재귀)
def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# BFS 함수
def bfs(start):
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# DFS 실행
dfs_visited = [False] * (n + 1)
dfs(v, dfs_visited)
print()  # 줄바꿈

# BFS 실행
bfs(v)
