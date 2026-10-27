s=input()
s=int(s+s[-2::-1])
f=True
for i in range(2,int(s**0.5)+1):
    if s%i==0:
        f=False
        break
if f:
    print("prime")
else:
    print("noprime")