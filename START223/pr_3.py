# Problem:
# https://www.codechef.com/START223D/problems/SCHOOLTRIP

t=int(input())

for _ in range(t):
    n,x,k = map(int, input().split())
    
    rem = x % k
    
    l_c =rem
    
    if x+(k-rem)<=n:
        u_c =k-rem
    else:
        u_c =float('inf')
    
    c_z =x
    
    print(min(l_c, u_c, c_z))
        