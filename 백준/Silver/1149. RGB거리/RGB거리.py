N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

# DP 배열 초기화 (첫 번째 집은 선택 비용 그대로)
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

# DP 테이블 채우기
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # 빨강
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # 초록
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # 파랑

# 결과 출력: 마지막 집에서 세 색 중 최소 비용
print(min(dp[N-1]))