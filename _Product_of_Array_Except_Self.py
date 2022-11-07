n=int(input())
l=list(map(int,input().split()))
if 0 not in l:
    f=1
    for i in l:
        f*=i
    for i in l:
        print(f//i,end=' ')
elif l.count(0)>=2:
    for i in l:
        print(0,end=' ')
else:
    for i in l:
        if i!=0:
            print(f//i,end=' ')
        else:
            print(f,end=' ')