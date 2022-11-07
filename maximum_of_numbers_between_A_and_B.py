n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
for i in range(k[1],k[0]-1,-1):
    if i in l:
        print(i)
        break
else:
    print(-1)