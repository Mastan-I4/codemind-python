def vow(s):
    for i in s:
        if i not in "aeiou":
            return False
    return True
s1=""
s=input()
for i in range(len(s)):
    for j in range(len(s)):
        if vow(s[i:j+1]):
            if len(s[i:j+1])>len(s1):
                s1=s[i:j+1]
print(len(s1))