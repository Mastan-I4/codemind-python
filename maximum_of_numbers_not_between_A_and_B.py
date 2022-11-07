n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
l.sort(reverse=True)
for i in l:
    if i not in range(k[0],k[1]+1):
        print(i)
        break
else:
    print(-1)