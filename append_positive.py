#Append positive numbers in a list until a negative number is entered

positive_num=[]
while True:
    num=int(input("Enter the number : -"))
    if num<0:
        break
    positive_num.append(num)

print(positive_num)