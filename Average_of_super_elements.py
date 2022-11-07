n=int(input())
l=list(map(int,input().split()))
k=[]
for i in set(l):
    if i==l.count(i):
        k.append(i)
if k==[]:
    print(-1)
else:
    p=round(sum(k)/len(k),2)
    print("{:.2f}".format(p))