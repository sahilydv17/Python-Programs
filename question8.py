#to check if triangle is equilateral , isosceles or scalene
sides_equal = int(input("how many sides of the triangle is equal "))
if sides_equal == 3:
    print("it is a equilateral triangle.")
elif sides_equal == 2:
    print("it is a isosceles triangle.")
else:
    print("it is a scalene triangle.")
