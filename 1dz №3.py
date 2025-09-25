A=list(map(int,input().split()))
q=1
for i in A:
    q=q*i
print(q**(1/len(A)))
