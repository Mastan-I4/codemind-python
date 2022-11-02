c=0
s=input()
for i in s:
    if i.isnumeric():
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")