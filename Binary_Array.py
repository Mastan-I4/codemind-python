n=int(input())
l=list(map(int,input().split()))
for i in l:
    if i not in range(0,2):
        print("False")
        break
else:
    print("True")