num = int(input('Enter a number: '))
sum = 0
temp = num
temp1 = num
x=0
while temp1>0:
    temp1 = temp1//10
    x=x+1
while temp>0:
    digit = temp%10
    i = digit ** x
    sum = sum + i
    temp=temp//10
if num==sum:
    print(num, 'is an Armstrong number.')
else:
    print(num, 'is not an Armstrong number.')
