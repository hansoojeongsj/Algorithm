import sys

# 수의 개수 N 입력
N = int(sys.stdin.readline())

# 빈 리스트 생성
arr = []

# N개의 수 입력 받기
# numbers 리스트에 추가
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# numbers 리스트를 오름차순으로 정렬
arr.sort()

# 정렬된 수를 한 줄씩 출력
for num in arr:
    print(num)