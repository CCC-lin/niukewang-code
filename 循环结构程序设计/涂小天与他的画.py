T=int(input())
for i in range(T):
    n=int(input())
    for i in range(1,n//2+1+1):
        print(" "*(n//2-i+1)+"*"*(2*i-1))
    for i in range(n//2,0,-1):
        print(" "*(n//2-i+1)+"*"*(2*i-1))