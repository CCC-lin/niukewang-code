T=int(input())
n={'zero':'0','two':'2','four':'4','six':'6','nine':'9'}
v=('0','2','4','6','9')
for _ in range(T):
    s=input()
    x=''
    for i in n.keys():
        if i in s:
            s=s.replace(i,n[i])
    for i in s:
        if i in v:
            x+=i
    print(x)