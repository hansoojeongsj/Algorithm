import sys

n = int(sys.stdin.readline())
meetings = []

for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append((s, e))

# 정렬 기준 함수 정의 (끝나는 시간, 시작 시간 순)
def sort_key(meeting):
    return (meeting[1], meeting[0])

meetings.sort(key=sort_key)

cnt = 1
end_time = meetings[0][1]

for i in range(1, n):
    if meetings[i][0] >= end_time:
        cnt += 1
        end_time = meetings[i][1]

print(cnt)
