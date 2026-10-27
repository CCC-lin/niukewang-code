a,b = map(int,input().split())
morning=list(map(int,input().split()))
night=list(map(int,input().split()))
s=sum(night)
y=[]
for i in range(a):
    x=morning[i]-night[i]
    y.append(x)
y.sort(reverse=True)
result=s+sum(y[:b])
print(result)