c=1
ma=1
s=input()
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        c=1
    if c>ma:
        ma=c
print(ma)