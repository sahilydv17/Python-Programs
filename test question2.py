#write a program to ptint fizz if number is divisible by 7
for i in range(1,51,1):
    if(i % 7 == 0):
       print(i,"fizz")
    elif(i%5==0):
        print(i,"buzz")
    elif(i%5 and i%7 ==0):
        print(i,"fizzbuzz")
