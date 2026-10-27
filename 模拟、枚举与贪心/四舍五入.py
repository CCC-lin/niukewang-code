n,t=map(int,input().split())
x=input()
if '.' not in x:
    print(x)
    exit()
a,b=x.split('.')
f=False
a=int(a)
while t!=0:
    for i in range(len(b)):
        if b[0]>='5':
            a+=1
            f=True
            break
        elif b[i]>='5':
            b=str(int(b[:i])+1)
            break
    t-=1
    if f:
        break
if f:
    print(a)
else:
    print(str(a)+'.'+b)