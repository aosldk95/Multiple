number = 1000
number3=[]
number5=[]
number15=[]
for i in range(0,number,3):
    number3.append(i)
for i in range(0,number,5):
    number5.append(i)
for i in range(0,number,15):
    number15.append(i)
print(sum(number3)+sum(number5)-sum(number15))

    
