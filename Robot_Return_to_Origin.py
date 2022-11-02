x=0
y=0
s=input()
for i in s:
    if i=="U":
        y+=1
    elif i=="D":
        y-=1
    elif i=="L":
        x-=1
    else:
        x+=1
if(x==0 and x==y):
    print("True")
else:
    print("False")