num=int(input("enter a three digit number "))
a=num%10
num=num//10
b=num%10
num=num//10
reverse=((a*100)+(b*10) +num)
print(reverse)