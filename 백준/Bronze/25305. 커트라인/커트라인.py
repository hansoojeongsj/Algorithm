# 입력 받기
N, k = map(int, input().split())
scores = list(map(int, input().split()))

# 점수 내림차순 정렬
scores.sort(reverse=True)

# 커트라인 출력
print(scores[k - 1])