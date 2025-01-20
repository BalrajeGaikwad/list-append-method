#append prime number from 1 to 30 in a list

l=[]

for i in range(2,31):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
        else:
            l.append(i)

print(l)