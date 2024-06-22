string1 = input("Enter a string: ")
length = len(string1)
string2 = string1[::-1]
if string1 == string2:
    print("It is a palindrome")
else:
    print("It is not a palindrome")