n=int(input())
l=list(map(int,input().split()))
k=[]
for i in l:
    if i not in k:
        print(i,end=' ')
        k.append(i)