n = int(input())
A = list(map(int, input().split()))

# A의 값과 원래 인덱스를 저장
temp = []
for i in range(n):
    temp.append([A[i], i])  # [값, 원래 위치]

# 값 기준으로 오름차순 정렬
temp.sort()

# P 배열을 만들기 위한 리스트 초기화
P = [0] * n

# 정렬된 순서대로 순위 번호를 원래 위치에 기록
for i in range(n):
    value, original_index = temp[i]
    P[original_index] = i

# 출력
print(*P)