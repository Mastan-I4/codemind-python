n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    if l[i]==l.count(l[i]) and l[i] not in k:
        k.append(l[i])
if k==[]:
    print(-1)
else:
    for i in k:
        print(i,end=' ')