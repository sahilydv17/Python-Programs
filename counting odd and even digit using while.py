num = int(input("enter any number"))
count = 0
count1 = 0
while(num>0):
    if (num % 2 == 0):
        count = count+1
        num = num//10
    elif(num % 2 != 0):
        count1 = count1 + 1
        num = num//10
print(count)
print(count1)
