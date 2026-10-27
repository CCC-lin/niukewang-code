L,R=map(int,input().split())
num=0
for i in range(L,R+1):
    num+=str(i).count('2')
print(num)