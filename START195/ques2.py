# Question:  https://www.codechef.com/problems/FAIL

t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map(int, input().split()))
    
    s, avg = 0, 0
    isPass = True
    
    for i in range(n):
        s += arr[i]
        avg = s/(i+1)
        
        if avg < 40:
            isPass = False
            break
        
    print("Yes") if isPass == True else print("No")