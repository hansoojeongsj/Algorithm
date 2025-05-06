import sys
import math

# 입력
N, L = map(int, sys.stdin.readline().split())
pools = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 시작 위치 기준으로 정렬
pools.sort()

count = 0
cur_pos = 0  # 현재 덮은 마지막 위치

for start, end in pools:
    # 현재 널빤지가 커버한 이후부터만 처리
    if cur_pos < start:
        cur_pos = start

    # 덮어야 할 길이 계산
    need_len = end - cur_pos
    if need_len > 0:
        planks = math.ceil(need_len / L)
        count += planks
        cur_pos += planks * L

print(count)
