n=int(input())
l=list(map(int,input().split()))
c1=0
c2=0
for i in range(len(l)):
    if l[i]%2==0:
        c1+=l[i]
    else:
        c2+=l[i]
print(c1)
