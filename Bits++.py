n=int(input())
c=0
for i in range(n):
    k=input()
    if "++" in k:
        c+=1
    else:
        c-=1
print(c)