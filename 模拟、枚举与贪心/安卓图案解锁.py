pos ={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
while True:
    try:
        s=input().strip()
        nums=list(map(int,s))
        v=set()
        ok=True
        for i in range(len(nums)):
            n=nums[i]
            if n in v:
                ok = False
                break
            if i>0:
                p=nums[i-1]
                x1,y1=pos[p]
                x2,y2=pos[n]
                mid_x=(x1+x2)/2
                mid_y=(y1+y2)/2
                if mid_x.is_integer() and  mid_y.is_integer():
                    mid_x=int(mid_x)
                    mid_y=int(mid_y)
                    mid_num=-1
                    for k,(x,y) in pos.items():
                        if x == mid_x and y == mid_y:
                            mid_num=k
                            break
                    if mid_num not in v:
                        ok=False
                        break
            v.add(n)
        if ok:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break