t=int(input())

for _ in range(t):
    s=list(input())
    res = 0

    if s[0] == 'u':
        s[0] = 's'
        res+=1
        
    if s[-1] == 'u':
        s[-1] = 's'
        res += 1

    cnt=0
    for ch in s:
        if ch == 'u':
            cnt+=1
        else:
            res += cnt//2
            cnt=0

    print(res)