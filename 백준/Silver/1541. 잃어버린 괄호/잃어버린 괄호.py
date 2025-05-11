expression = input().split('-')

# 첫 번째 그룹은 그냥 더한다.
initial = sum(map(int, expression[0].split('+')))

# 나머지 그룹은 다 더한 뒤 뺀다.
rest = 0
for part in expression[1:]:
    rest += sum(map(int, part.split('+')))

print(initial - rest)