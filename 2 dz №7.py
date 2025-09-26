a=input().split()
for i in range(len(a)):
    s=0
    n=0
    for j in range(len(a)):
        if a[i]==a[j]:
            s+=1
        if(s>n):
            n=s
            a_max=a[i]
print(a_max)
