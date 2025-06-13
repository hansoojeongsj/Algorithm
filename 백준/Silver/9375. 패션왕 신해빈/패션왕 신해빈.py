import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    wears = {}
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        name, type = sys.stdin.readline().strip().split()
        if type in wears:
            wears[type].append(name)
        else:
            wears[type] = [name]
    
    cnt = 1
    
    for x in wears:
        cnt *= (len(wears[x]) + 1)
	
    print(cnt-1)
