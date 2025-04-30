import sys
input = sys.stdin.readline
N, M, K = list(map(int, input().split()))
team = 0
while True:
    N = N - 2
    M = M - 1
    if N < 0 or M < 0 or (N+M) < K:
        break
    team = team + 1
print (team)