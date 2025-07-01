amount=int(input("enter a amount "))
n500=amount//500
ramount=amount-(n500*500)
n200=ramount//200
ramount=ramount-(n200*200)
n100=ramount//100
ramount=ramount-(n100*100)
n50=ramount//50
ramount=ramount-(n50*50)
n10=ramount//10
remaining=ramount%10
print("total notes of 500 is: ",n500)
print("total notes of 200 is :", n200)
print("total notes of 100  is :",n100)
print("total number of 50 is :",n50)
print("total number of 10 is :",n10)
print(remaining)