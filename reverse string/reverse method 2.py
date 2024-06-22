string1 = input("Enter a string: ")
list1 = []
for i in string1:
    list1.append(i)
list1.reverse()
for i in list1:
    print(i, end="")