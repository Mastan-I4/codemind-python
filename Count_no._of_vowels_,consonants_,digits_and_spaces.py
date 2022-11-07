s=input()
v=0
c=0
d=0
w=0
for i in s:
    if i in "aeiouAEIOU":
        v+=1
    elif i.isalpha():
        c+=1
    if i.isdigit():
        d+=1
    if i==" ":
        w+=1
print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",w)