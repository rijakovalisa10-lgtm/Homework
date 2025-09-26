a=input().split()
a[:-1:2], a[1::2] = a[1::2], a[:-1:2]
print(a)
