s=input()
x=ord(s)-ord('A')+1
for i in range(1,x+1):
    print(" "*(x-i),end="")
    for j in range(i):
        print(chr(ord('A')+j),end="")
    for j in range(i-1,0,-1):
        print(chr(ord('A')+j-1),end="")
    print()   