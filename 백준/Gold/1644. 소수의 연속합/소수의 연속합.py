import sys

N = int(sys.stdin.readline())

# 예외 처리: 1 이하는 소수 없음
if N < 2:
    print(0)
    exit()

# 에라토스테네스의 체로 소수 구하기
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, N + 1, i):
            is_prime[j] = False

primes = [i for i, val in enumerate(is_prime) if val]

# 투 포인터 알고리즘
count = 0
start = 0
end = 0
current_sum = 0

while True:
    if current_sum >= N:
        if current_sum == N:
            count += 1
        current_sum -= primes[start]
        start += 1
    elif end == len(primes):
        break
    else:
        current_sum += primes[end]
        end += 1

print(count)