n=int(input())
l=list(map(int,input().split()))
l=l[::-1]
for i in range(len(l)):
    if l[i]%2==0:
        print(l[i])
        break