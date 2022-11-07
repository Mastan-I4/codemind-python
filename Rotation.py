t=int(input())
for k in range(t):
    n=list(map(int,input().split()))
    l=list(map(int,input().split()))
    if n[1]>len(l):
        n[1]=n[1]%len(l)
    m=l[(len(l)-n[1]):]+l[:(len(l)-n[1])]
    for i in range(len(m)-1):
        print(m[i],end=' ')
    print(m[len(m)-1])