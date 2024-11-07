marks1 = float(input("Enter marks scored in 1st subject: "))
marks2 = float(input("Enter marks scored in 2nd subject: "))
marks3 = float(input("Enter marks scored in 3rd subject: "))
marks4 = float(input("Enter marks scored in 4th subject: "))
marks5 = float(input("Enter marks scored in 5th subject: "))

percentage = ((marks1+marks2+marks3+marks4+marks5)/500)*100

print("Percentage scored by student:", percentage)

if percentage >= 90:
    print("Student scored 'A' grade.")
if percentage < 90  > 70:
    print("Student scored 'B' grade.")
if percentage < 70 > 50:
    print("Student scored 'C' grade.")
if percentage < 50:
    print("Student scored 'D' grade.")
