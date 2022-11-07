n=int(input())
l=list(map(int,input().split()))
k=[]
f=1
for i in l:
    if l.count(i)==1:
        f=0
        print(i,end=' ')
        k.append(i)
if f==1:
    print(-1)