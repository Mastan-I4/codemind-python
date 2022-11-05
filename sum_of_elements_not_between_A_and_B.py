n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
c=0
for i in l:
    if i not in range(k[0],k[1]+1):
        c+=i
print(c)