string1 = input("Enter a string: ")
set1 = {}

for i in range(len(string1)):
    if string1[i] in "aeiou":
        set1[i] = string1[i]
count1 = (len(set1))
print(f"{count1} vowels are present in {string1}")
for i in set1:
    print(set1[i], end=" ")

