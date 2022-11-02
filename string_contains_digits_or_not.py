n=int(input())
for i in range(n):
    x=input()
    for j in x:
        if j.isnumeric():
            print("Yes")
            break
    else:
        print("No")