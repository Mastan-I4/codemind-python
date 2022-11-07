n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=[]
for i in l:
    if k==l.count(i) and i not in f:
        f.append(i)
if f==[]:
    print(-1)
else:
    for i in f:
        print(i,end=' ')