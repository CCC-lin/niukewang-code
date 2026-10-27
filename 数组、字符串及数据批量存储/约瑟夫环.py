a,b,c=map(int,input().split())
people=list(range(a))
d=b
while len(people)>1:
    d=(d+c-1)%len(people)
    people.pop(d)
print(people[0])