num1 = int(input("Enter a number to find its factorial: "))
fact = 1
for i in range(1, num1 + 1):
    fact = fact * i
print(fact)