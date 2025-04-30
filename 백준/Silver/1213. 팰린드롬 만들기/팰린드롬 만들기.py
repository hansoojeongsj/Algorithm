# 팰린드롬 : 앞에서 읽어도 뒤에서 읽어도 똑같은 문자열
# 알파벳 빈도수 알아야, 모든 문자열 짝수개 또는 하나의 문자만 홀수개, 나머지 문자열은 짝수개

name = input() 

count = dict()
keys = sorted(list(set(name)))
odd = []
for key in keys: # 사전순으로 절반 문자열 구성
    cnt = name.count(key)
    count[key] = cnt
    if cnt % 2:
        odd.append(key)

if len(odd) > 1:
    print("I'm Sorry Hansoo")

else:
    result = ''

    for key in keys: # Ex) AAB 생성
        result += key * (count[key] // 2)

    if odd: # 홀수 개수 문자가 있다면 (길이 홀수인 팰린드롬)
        result += odd[0] + result[::-1]
    else: # 모두 짝수인 경우 (길이 짝수인 팰린드롬)
        result += result[::-1]

    print(result)
