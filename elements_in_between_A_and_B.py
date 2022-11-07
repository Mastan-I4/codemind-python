n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
f=1
for i in l:
    if i>=k[0] and i<=k[1]:
        f=0
        print(i,end=' ')
if f==1:
    print(-1)