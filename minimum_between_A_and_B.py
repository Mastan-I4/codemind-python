n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
for i in range(k[0],k[1]+1):
    if i in l:
        print(i)
        break
else:
    print(-1)