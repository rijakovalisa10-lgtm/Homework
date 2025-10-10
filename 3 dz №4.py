size = int(input())
symb = str(input())
for i in range(1, size//2+(size%2)+1):
    print(symb*i)
for q in range(size//2, 0, -1):
    print(symb*q)
    