n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=1
for i in l:
    if i not in range(k[0],k[1]+1):
        print(i,end=' ')
        c=0
if c==1:
    print(-1)