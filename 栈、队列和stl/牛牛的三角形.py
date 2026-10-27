n=int(input())
a=list(map(int,input().split()))
a.sort()
f=True
for i in range(n-2):
    if a[i]+a[i+1]>a[i+2]:  
        print(f"{a[i]} {a[i+1]} {a[i+2]}")
        f=False
        break
if f:
    print("No solution")