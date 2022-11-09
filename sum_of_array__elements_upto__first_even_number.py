n=int(input())
l=list(map(int,input().split()))
c=0
f=1
for i in l:
    if i%2==0:
        print(c)
        f=0
        break
    else:
        c+=i
if f==1:
    print(c)