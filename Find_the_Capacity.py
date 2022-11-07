l=list(map(int,input().split()))
p=(l[0]*l[1]*l[2]*2*512)//1024
txt = "{price:}KB"
print(txt.format(price = p))