x,y=map(int,input().split())
count=0
for i in range(x,y+1):
    s=str(i)
    a=0
    for j in s:
        a+=int(j)
    if a%5==0:
        count+=1
print(count)