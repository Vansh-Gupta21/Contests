# Problem
# https://www.codechef.com/START223D/problems/ADD1234

t=int(input())

for _ in range(t):
    x,y,z = map(int, input().split())
    print(min(x,z)+y//2)