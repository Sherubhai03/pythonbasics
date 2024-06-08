list1 = [1, 2, 3, 4, 5, "abc", 6, 7]
list1.remove("abc")  #remove keyword must take 1 parameter that we want to remove
print(list1)
list1.pop()  #remove last element of the list
print(list1)
list1.pop(3)  #remove element at index 3
print(list1)
list1.append(9)  # add element to the end of the list
print(list1)
list1.insert(2, 10)  #add element at index 2
print(list1)

#extend keyword used to add multiple elements to the end of list like array and string
list1.extend([11, 12, 13])  #add multiple elements to the end of list
print(list1)
list1.extend("ab")  #add multiple elements to the end of list
print(list1)
print(list1.index(12))  #return index of element
