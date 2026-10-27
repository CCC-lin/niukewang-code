import sys
for c in sys.stdin:
    c=c.strip()
    if not c:
        continue
    a,b=map(int,c.split())
    num=0
    for i in range(1,a+1):
        d=i
        while d>0:
            x=d%10
            d=d//10
            if x==b:
                num+=1
    print(num)
