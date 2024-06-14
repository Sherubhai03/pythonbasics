side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))
if side1 == side2 and side2 == side3:
    print("Its a Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Its a Isosceles")
else:
    print("Its a Scalene")