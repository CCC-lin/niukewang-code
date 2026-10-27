L,M=map(int,input().split())
trees=[1]*(L+1)
for _ in range(M):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        trees[i]=0
num=0
for i in range(L+1):
    if trees[i]==1:
        num+=1
print(num)