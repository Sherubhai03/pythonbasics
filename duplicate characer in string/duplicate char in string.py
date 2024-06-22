string1 = input("Enter a string: ")
list1 = []
flag = 0
for i in range(len(string1)):
    for j in range(i+1, len(string1)):
        if string1[i] == string1[j]:
            list1.append(string1[i])
            flag = 1

if flag == 0: print("No duplicate character found")
else:
    print("Duplicate characters are: ", end="")
    for i in list1:
        print(i, end="")

