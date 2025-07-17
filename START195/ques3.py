# Question:  https://www.codechef.com/problems/MARBCOLL

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    
    arr = list(map(int, input().split()))
    
    mp = {}
    
    for num in arr:
        if num in mp:
            mp[num] += 1
        else:
            mp[num] = 1
    
    print(m-len(mp))