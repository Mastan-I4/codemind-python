n=int(input())
l=list(map(int,input().split()))
k=int(input())
c=0
l.sort()
for i in l:
    if i<=k:
        c+=i
print(c)