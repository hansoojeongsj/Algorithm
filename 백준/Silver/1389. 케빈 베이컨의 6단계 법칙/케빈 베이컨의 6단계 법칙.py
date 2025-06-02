from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (n+1)
    dist[start] = 0
    q = deque([start])
    while q:
        x = q.popleft()
        for friend in graph[x]:
            if dist[friend] == -1:
                dist[friend] = dist[x] + 1
                q.append(friend)
    return sum(dist[1:])  # 0번째 인덱스는 없으니까 제외

answer = 0
min_sum = 10**9

for i in range(1, n+1):
    total = bfs(i)
    if total < min_sum:
        min_sum = total
        answer = i

print(answer)
