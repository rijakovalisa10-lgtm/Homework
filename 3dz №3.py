def nod(a,b):
    if a*b==0:
        return a+b
    if a<b:
        return nod(a,b%a)
    else:
        return nod(a%b,b)
a,b=map(int,input().split())
n=nod(a,b)
mas=[]
for x in range(-1000,1000):
    for y in range(-1000,1000):
        if a*x+b*y==n:
            mas.append([x,y])
mas.sort(key=lambda x:abs(x[0])+abs(x[1]))
print(*mas[0],n)


