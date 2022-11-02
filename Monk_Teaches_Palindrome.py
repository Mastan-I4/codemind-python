n=int(input())
for i in range(n):
    s=input()
    if s!=s[::-1]:
        print("NO")
    else:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")