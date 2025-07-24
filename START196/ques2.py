# Question:   https://www.codechef.com/problems/MORECOOK

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    k = max(min(arr)+1, c)
    
    while k in arr:
        k += 1
        
    print(k-c)