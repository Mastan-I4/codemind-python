n=int(input())
l=list(map(int,input().split()))
m=[]
k=[]
for i in l:
    if i%2==0:
        m.append(i)
    else:
        k.append(i)
for i in k:
    print(i,end=' ')
for i in m:
    print(i,end=' ')