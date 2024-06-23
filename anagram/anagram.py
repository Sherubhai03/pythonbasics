string1 = input("Enter a string: ").lower()
string2 = input("Enter another string: ").lower()
if len(string1) != len(string2):
    print("given string are not anagram.")
else:
    if sorted(string1) == sorted(string2):
        print("Given string are anagram.")
    else:
        print("Given string are not anagram.")