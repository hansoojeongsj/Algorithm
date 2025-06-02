# 경로 찾기
def dfs(s):   #방문할 정점이 없을 때 까지 재귀
    for i in range(n):
        if visited[i] == '0' and graph_list[s][i] == 1:
            visited[i] = '1'    #방문할 정점
            dfs(i)  #다음 정점에 대해 실행

n = int(input())
graph_list = []
for i in range(n):
    graph_list.append(list(map(int,input().split())))   #인접행렬 구성

for i in range(n):
    visited = ['0' for _ in range(n)]  # 정점 방문 초기화
    dfs(i)
    print(' '.join(visited))    #공백 포함한 문자열로 변환
