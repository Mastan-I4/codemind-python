n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
f=1
l.sort()
for i in l:
    if i not in range(k[0],k[1]+1):
        f=0
        print(i)
        break
if f==1:
    print(-1)