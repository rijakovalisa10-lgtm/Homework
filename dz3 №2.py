n=int(input())
kn=[]
def prost(n):
    if n !=1:
        for i in range(2,n+1):
            if n % i ==0:
                kn.append(i)
                prost(n//i)
                break
prost(n)
print(kn)

