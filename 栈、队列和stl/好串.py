s=input().strip()
while 'ab' in s:
    s = s.replace('ab','')
if len(s) == 0:
    print("Good")
else:
    print("Bad")