a=list(map(int,input().split()))
b=[]
for i in range(10):
    if a[i]%2==1:
        b.append(i)
if len(b)>1:
    print(-1)
else:
    mi=''
    if len(b)==1:
        x=b[0]
        mi=str(x)
        a[x]-=1
    left=''
    for i in range(1,10):
        if a[i]>0:
            left+=str(i)
            a[i]-=2
            break
    for i in range(10):
        c=a[i]//2
        left+=str(i)*c
    if left =='':
        print(mi)
    else:
        result=left+mi+left[::-1]
        if result[0]=='0':
            print(-1)
        else:
            print(result)
