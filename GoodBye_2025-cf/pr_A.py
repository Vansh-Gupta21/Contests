t=int(input())

for _ in range(t):
    s=input()
    cnt=s.count('Y')
    print("No") if cnt>1 else print("Yes")