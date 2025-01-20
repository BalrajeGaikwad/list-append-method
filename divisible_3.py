#Append numbers divisible by 3 but not by 5

l=[]

for i in range(1,21):
    if i%3==0 and i%5!=0:
        l.append(i)

print(l)