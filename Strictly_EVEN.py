n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    if l[i]%2==0 and i%2!=0:
        print("False")
        break
else:
    print("True")