#printing digits of a number
#if you have to find the digits of a number you have to devide number by 10 the remainder will be the last digit.
#when you know till where the loop will work we will use for loop
#when you dont know till where the loop will work we will use while loop
num = int(input("enter number"))
while(num>0):
    remainder=num%10
    print(remainder)
    #decrease the number by removing unit digit.
    num = num//10
