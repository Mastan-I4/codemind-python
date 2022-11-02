s=input()
s1=""
k=""
for i in range(len(s)):
    if s[i] in "aeiou":
        s1+="V"
    else:
        s1+="C"
for i in range(len(s1)-1):
    if s1[i]!=s1[i+1]:
        k+=s1[i]
k+=s1[len(s)-1]
print(k)