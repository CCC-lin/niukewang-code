n=int(input())
x=0
for i in range(1,n+1):
    for j in range(0,i):
        x+=1
        print(f"{x:4d}",end="")
    print()