#Append numbers greater than 10 but less than 15


num=[]

for i in range(1,16):
    if i>=10 and i<=15:
        num.append(i)

print(num)