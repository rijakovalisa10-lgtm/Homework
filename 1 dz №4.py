f=open('input.txt', 'r')
f.read()
numbers=list(map(int, input()))
operation=input().split()
if operation=="+":
    result=sum(numbers)
elif operation=="-":
    result=numbers[0]
    for num in numbers[1:]:
        result-=num
elif operation =='*':
    result=1
    for num in numbers:
        result*=num
f=open("output.txt", "w") as file:
    file.write(str(result))
f.close('input.txt')


