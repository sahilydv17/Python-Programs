#print the count of digits in a number
number = int(input("Please enter a number: "))
count = 0
while(number>0):
    number = number // 10 
    count = count+1
print("Number of digits:", count)
