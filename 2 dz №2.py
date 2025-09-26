g,s=input()split()
g=int(g)
group_len=len(s)//g
result=[]
for i in range(0, len(s), group_len):
    res +=s[i: i+g][::-1]
print(res)