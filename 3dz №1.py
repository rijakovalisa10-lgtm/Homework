if n<=0:
    return 'число>0'
elif n==1:
    return 0
elif n==2:
    return 1
a,b=0,1
for_in range(2,n):
a,b=b, a+b
return b
N=int(input('омер числа Фибоначчи:'))
result=fibonacci(N)
print(f"{N}-e число Фибоначчи равно:{result}")

except ValueError:
print("ввести целое число")
