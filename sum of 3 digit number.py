num=int(input("enter a three digit number"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
sum=a+b+c
print("sum of three digits of number is :",sum)
