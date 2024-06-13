Num1 = int(input("Enter the the marks: "))
if Num1 > 100:
    print("Invalid marks")
elif  Num1 >= 90 and Num1 <= 100:
    print("A")
elif Num1 >= 80 and Num1 < 90:
    print("B")
elif Num1 >= 70 and Num1 < 80:
    print("C")
elif Num1 >= 60 and Num1 < 70:
    print("D")
else:
    print("F")