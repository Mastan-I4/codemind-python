l=''
s=input()
for i in s:
    if i in "aeiouAEIOU":
        l+=i
k=""
m=0
l=l[::-1]
for j in s:
    if j in "aeiouAEIOU":
        k+=l[m]
        m+=1
    else:
        k+=j
print(k)