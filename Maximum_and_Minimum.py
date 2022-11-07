n=int(input())
l=list(map(int,input().split()))
k=[]
for i in set(l):
    if i==l.count(i):
        k.append(i)
if k==[]:
    print(-1)
else:
    print(k[0],k[len(k)-1])