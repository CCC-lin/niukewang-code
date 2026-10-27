n=int(input())
moon=list(map(int,input().split()))
if n==1:
    if moon[-1]==0:
        print("UP")
    elif moon[-1]==15:
        print("DOWN")
    else:
        print(-1)
else:
    if moon[-1] > moon[-2]:
        if moon[-1]==15:
            print("DOWN")
        else:
            print("UP")
    elif moon[-1] < moon[-2]:
        if moon[-1]==0:
            print("UP")
        else:
            print("DOWN")