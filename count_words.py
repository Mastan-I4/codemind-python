s=input()
p=s.split(' ')
c=0
for i in p:
    if i[0] in "aeiouAEIOU" and i[len(i)-1] not in "aeiouAEIOU":
        c+=1
print(c)