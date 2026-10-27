import sys

def days(y,m):
    if m in(1,3,5,7,8,10,12):
        return 31
    if m in(4,6,9,11):
        return 30
    if m==2:
        if y % 400==0 or (y%4==0 and y%100 !=0):
            return 29
        else :return 28

for x in sys.stdin:
    lst=x.strip().split()
    y,m,n=int(lst[0]),int(lst[1]),int(lst[2])
    d=days(y,m)
    count=0
    b=str(n)
    for i in range(1,d+1):
        date=f'{y:04d}-{m:02d}-{i:02d}'
        count+=date.count(b)
    print(count)